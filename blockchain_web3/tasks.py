from datetime import timedelta
import uuid
from celery import shared_task
from django.utils import timezone
from core.models import CardPackType, CustomUser, AssignedCardPack, AssignedPlayer, NftBucket, StoreProduct, Transactions, StoreProductTransactions
from blockchain_web3.services import CryptoTransactionService
from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
import os
import boto3
import requests
import logging

# Set up logging
logger = logging.getLogger(__name__)

WEB3_PROVIDER_URI = os.getenv("WEB3_PROVIDER_URI")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
FOLDER = os.getenv("FOLDER")
CONTRACT_ADDRESS_SEASON = os.getenv("CONTRACT_ADDRESS_SEASON")
FOLDER_SEASON = os.getenv("FOLDER_SEASON")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
S3_BUCKET = os.getenv("S3_BUCKET")
PUBLIC_ADDRESS = os.getenv("PUBLIC_ADDRESS")


def get_metadata_url(player):
    rarity = player.rarity
    nft_bucket = NftBucket.objects.get(pk=player.player_nft_id)

    if rarity == "common":
        return nft_bucket.common_metadata
    elif rarity == "uncommon":
        return nft_bucket.uncommon_metadata
    elif rarity == "rare":
        return nft_bucket.rare_metadata
    elif rarity == "ultra_rare":
        return nft_bucket.ultra_rare_metadata
    elif rarity == "legendary":
        return nft_bucket.legendary_metadata
    else:
        return None

def mint_nfts_for_cardpacks(card_packs):
    web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URI))
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to playersabi.json
    json_path = os.path.join(current_dir, 'playersabi.json')

    # Open and load the JSON file
    with open(json_path) as f:
        contract_abi = json.load(f)
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name="us-east-1"
    )

    for pack in card_packs:
        print(f"Processing card pack {pack.id}")
        try:
            # Get the CustomUser wallet address
            user = CustomUser.objects.get(pk=pack.user_id)
            # If pack.collectio is season then folder is FOLDER_SEASON and contract address is CONTRACT_ADDRESS_SEASON
            if pack.collection == "season":
                FOLDER = FOLDER_SEASON
                CONTRACT_ADDRESS = CONTRACT_ADDRESS_SEASON
            if not user.wallet_address:
                logger.warning(f"User {user.id} does not have a wallet address, skipping")
                continue

            # Get the NFT IDs and metadata URLs from the assigned players
            nft_ids = []
            metadata_files = []
            for player_nft_id in pack.card_ids:
                assigned_player = AssignedPlayer.objects.get(id=player_nft_id)
                nft_ids.append(int(assigned_player.nft_id))

                metadata_url = get_metadata_url(assigned_player)
                if metadata_url:
                    response = requests.get(metadata_url)
                    if response.status_code == 200:
                        metadata = response.json()
                        metadata_files.append({
                            'token_id': assigned_player.nft_id,
                            'metadata': metadata
                        })
                    else:
                        logger.warning(f"Failed to fetch metadata from {metadata_url}, received status code {response.status_code}")
                else:
                    logger.warning(f"No metadata URL found for player {assigned_player.id} with rarity {assigned_player.rarity}")
            userWallet = user.wallet_address
            # Convert userWallet to string
            to = str(userWallet)
            ids = nft_ids
            # Convert to list of integers
            ids = [int(i) for i in ids]
            # Prepare the   transaction
            nonce = web3.eth.get_transaction_count(PUBLIC_ADDRESS)

            # Upload metadata to S3
            for metadata in metadata_files:
                metadata_key = f"{FOLDER}/{metadata['token_id']}"
                s3_client.put_object(
                    Bucket=S3_BUCKET,
                    Key=metadata_key,
                    Body=json.dumps(metadata['metadata']),
                    ContentType='application/json'
                )
                print(f"Metadata for token ID {metadata['token_id']} uploaded to S3")

            txn = contract.functions.batchMint(to, ids).build_transaction({
                'nonce': nonce,
                'from': PUBLIC_ADDRESS
            })
            # Sign and send the transaction
            signed_txn = web3.eth.account.sign_transaction(txn, PRIVATE_KEY)
            txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

            # Wait for the transaction to be mined
            receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
            
            # Mark the pack as revealed
            pack.revealed = True
            pack.revealed_at = timezone.now()
            pack.save()
            print(f"Successfully minted NFTs for card pack {pack.id} to {user.wallet_address}")

        except Exception as e:
            logger.error(f"Error minting NFTs for card pack {pack.id}: {str(e)}")
            print(f"Error minting NFTs for card pack {pack.id}: {str(e)}")

@shared_task
def process_mint_nfts_for_expired_cardpacks():
    print("Starting mint_nfts_for_expired_cardpacks task")
    # Query for assigned card packs that are older than 48 hours and not revealed
    threshold_time = timezone.now() - timedelta(hours=50)
    try:
        # Query for all assigned card packs
        card_packs = AssignedCardPack.objects.filter(
            opened=True,
            opened_at__lte=threshold_time,
            revealed=False
        )
        print(f"Found {card_packs.count()} card packs to process")

        for pack in card_packs:
            if pack.store_transaction_id and not pack.refunded:
                print(f"Processing minting for card pack {pack.id}")
                mint_nfts_for_cardpacks([pack])
            else:
                print(f"Removing card_ids for card pack {pack.id} due to missing store_transaction_id or refunded status")
                # Remove card_ids and mark the pack as revealed
                pack.revealed = True
                pack.revealed_at = timezone.now()
                pack.save(update_fields=['revealed', 'revealed_at'])

    except Exception as e:
        logger.critical(f"Critical error in mint_nfts_for_expired_cardpacks: {str(e)}")
        
@shared_task
def process_pending_crypto_transactions():
    print("Starting process_pending_crypto_transactions task")
    
    # Define the contract addresses for GAME and LAPT tokens
    GAME_CONTRACT_ADDRESS = os.getenv('GAME_CONTRACT_ADDRESS')
    LAPT_CONTRACT_ADDRESS = os.getenv('LAPT_CONTRACT_ADDRESS')

    # Initialize the crypto transaction service
    crypto_service = CryptoTransactionService()

    # Fetch pending GAME and LAPT transactions
    transactions = Transactions.objects.filter(
        delivered=False,
        object_type__in=[Transactions.GAME, Transactions.LAPT]
    )
    print(f"Found {transactions.count()} transactions to process")

    for transaction in transactions:
        try:
            # Determine which token to send based on the object type
            token_contract_address = GAME_CONTRACT_ADDRESS if transaction.object_type == Transactions.GAME else LAPT_CONTRACT_ADDRESS
            token_type = "GAME" if transaction.object_type == Transactions.GAME else "LAPT"

            # Check if the wallet address is valid
            to_address = transaction.user.wallet_address
            if not to_address:
                logger.warning(f"Invalid wallet address for transaction {transaction.id}")
                # Mark the transaction as invalid or skip it
                transaction.status = 'invalid'
                transaction.save()
                continue  # Skip to the next transaction

            # Convert the transaction amount to Wei using Web3's `to_wei` method
            amount_in_wei = Web3.to_wei(transaction.amount, 'ether')

            # Send the cryptocurrency
            tx_hash = crypto_service.send_crypto(to_address, amount_in_wei, token_contract_address)

            # Update the transaction record as delivered
            transaction.delivered = True
            transaction.blockchain_uuid = tx_hash
            transaction.save()

            print(f"Successfully processed {token_type} transaction {transaction.id} for user {transaction.user_id}")

        except ValueError as ve:
            logger.error(f"Transaction {transaction.id} failed due to: {str(ve)}")
            print(f"Error processing transaction {transaction.id}: {str(ve)}")

        except Exception as e:
            logger.error(f"Error processing transaction {transaction.id}: {str(e)}")
            print(f"Error processing transaction {transaction.id}: {str(e)}")
@shared_task
def process_pending_cardpack_transactions():
    print("Starting process_pending_cardpack_transactions task")
    
    # Filter transactions for kickoff packs where delivery is false
    transactions = Transactions.objects.filter(
        delivered=False,
        object_type__in=[
            Transactions.SEASON_PACK_1,
            Transactions.SEASON_PACK_2,
            Transactions.SEASON_PACK_3
        ]
    )
    
    print(f"Found {transactions.count()} pending kickoff pack transactions to process")

    for transaction in transactions:
        try:
            # Get the user for the transaction
            user = transaction.user

            # Determine the card pack type based on the object_type
            if transaction.object_type == Transactions.SEASON_PACK_1:
                pack_type_uuid = 'f9adef06-85fd-498b-83f1-86ac25a16367'
                pack_type_staging_uuid = 'cd8fbb55-692d-491c-b4d3-4c1e42afec20'
                product_id = 'season_24_pack_1' 
                pack_name = "Season Pack 1"
            elif transaction.object_type == Transactions.SEASON_PACK_2:
                pack_type_uuid = 'd15c5248-cdfe-45bc-aec6-83dbd2814965'
                pack_type_staging_uuid = 'c0c6b781-14f8-40f8-aefb-19f56a4021d5'
                product_id = 'season_24_pack_2'
                pack_name = "Season Pack 2"
            elif transaction.object_type == Transactions.SEASON_PACK_3:
                pack_type_uuid = 'b4825f20-c611-4316-98ee-fc9433d9cd00'
                pack_type_staging_uuid = '064bfff2-4e8e-4701-bfc4-348a248df6be'
                product_id = 'season_24_pack_3'
                pack_name = "Season Pack 3"
            else:
                logger.error(f"Invalid transaction type {transaction.object_type} for transaction {transaction.id}")
                continue

            # Check if the user has a wallet address
            if not user.wallet_address:
                logger.warning(f"User {user.id} does not have a wallet address, skipping")
                continue

            # Fetch the StoreProduct instance
            product = StoreProduct.objects.get(store_product_id=product_id)

            # Create and save the StoreProductTransaction, linking it with the transaction
            store_transaction = StoreProductTransactions.objects.create(
                transaction=transaction,
                user=user,
                external_transaction_id=str(uuid.uuid4()),  # Generate a unique external transaction ID
                initiated=True,
                initiated_at=timezone.now(),
                product=product,
                origin_store="DivisionReward",  # Update with the actual origin store if needed
            )

            # Try to create and assign the new card pack with `pack_type`
            card_pack_type = None
            try:
                # Get the `CardPackType` instance for the primary `pack_type_uuid`
                card_pack_type = CardPackType.objects.get(pk=pack_type_uuid)
            except CardPackType.DoesNotExist:
                logger.warning(f"CardPackType with id {pack_type_uuid} does not exist, trying pack_type_staging {pack_type_staging_uuid}")
                print(f"CardPackType with id {pack_type_uuid} does not exist, trying pack_type_staging {pack_type_staging_uuid}")
                # Fallback to `pack_type_staging`
                try:
                    card_pack_type = CardPackType.objects.get(pk=pack_type_staging_uuid)
                except CardPackType.DoesNotExist:
                    logger.error(f"Both CardPackType {pack_type_uuid} and staging {pack_type_staging_uuid} do not exist.")
                    continue

            # Create the assigned card pack using the correct store_transaction's primary key (id)
            new_card_pack = AssignedCardPack(
                user=user,
                card_pack_type=card_pack_type,  # Assign the `CardPackType` instance
                opened=False,
                store_transaction=store_transaction  # Link to the `StoreProductTransactions` instance
            )
            new_card_pack.save()

            # Mark the transaction as delivered
            transaction.delivered = True
            transaction.save()

            print(f"Assigned {pack_name} to user {user.id} for transaction {transaction.id}")

        except Exception as e:
            logger.error(f"Error processing card pack transaction {transaction.id}: {str(e)}")
            print(f"Error processing card pack transaction {transaction.id}: {str(e)}")
