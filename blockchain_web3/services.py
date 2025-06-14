import json
import os
from web3 import Web3
import logging
from web3.gas_strategies.rpc import rpc_gas_price_strategy

logger = logging.getLogger(__name__)

class CryptoTransactionService:
    def __init__(self):
        WEB3_PROVIDER_URI = os.getenv("WEB3_PROVIDER_URI")
        PRIVATE_KEY = os.getenv("PRIVATE_KEY_TOKENS")

        self.web3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URI))
        self.private_key = PRIVATE_KEY

    def send_crypto(self, to_address, amount_in_wei, token_contract_address=None):
        account_from = {
            'private_key': self.private_key,
            'address': self.web3.eth.account.from_key(self.private_key).address
        }
        if token_contract_address:
            json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'GAME.json')
            with open(json_path) as f:
                contract_abi = json.load(f)
            contract = self.web3.eth.contract(address=token_contract_address, abi=contract_abi)
            self.web3.eth.set_gas_price_strategy(rpc_gas_price_strategy)
            tx = contract.functions.transfer(to_address, amount_in_wei).build_transaction({
                'from': account_from['address'],
                'gasPrice': self.web3.eth.generate_gas_price(),
                'nonce': self.web3.eth.get_transaction_count(account_from['address'])
            })
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, account_from['private_key'])
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
            tx_receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            if tx_receipt.status == 1:
                return tx_hash.hex()
            else:
                raise ValueError("Transaction failed")
        #     json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'GAME.json')
        #     with open(json_path) as f:
        #         contract_abi = json.load(f)
        #     contract = self.web3.eth.contract(address=token_contract_address, abi=contract_abi)
        #     account = self.web3.eth.account.privateKeyToAccount(self.private_key)
        #     self.web3.eth.default_account = account
        #     # send transaction
        #     tx_hash = contract.functions.transfer(to_address , amount_in_wei).transact()
        #     return tx_hash.hex()
        # else:
        #     account = self.web3.eth.account.privateKeyToAccount(self.private_key)
        #     self.web3.eth.default_account = account
        #     tx_hash = self.web3.eth.send_transaction({
        #         'from': account.address,
        #         'to': to_address,
        #         'value': amount_in_wei
        #     })
        #     return tx_hash.hex()
            
        # PUBLIC_ADDRESS = os.getenv("PUBLIC_ADDRESS_TOKENS")
        # nonce = self.web3.eth.get_transaction_count(PUBLIC_ADDRESS)

        # # Get the latest block to retrieve the base fee
        # latest_block = self.web3.eth.get_block('latest')
        # base_fee_per_gas = latest_block.get('baseFeePerGas', 0)

        # transaction = None  # Initialize variable

        # if token_contract_address:
        #     # Load the ABI from the JSON file
        #     current_dir = os.path.dirname(os.path.abspath(__file__))
        #     json_path = os.path.join(current_dir, 'GAME.json')

        #     try:
        #         with open(json_path) as f:
        #             contract_abi = json.load(f)

        #         # Interact with the token contract
        #         contract = self.web3.eth.contract(address=token_contract_address, abi=contract_abi)
                
        #         transaction = contract.functions.transfer(to_address, amount_in_wei).build_transaction({
        #             'nonce': nonce,
        #             'from': PUBLIC_ADDRESS,
        #             'gas': 2000000,
        #         })
                
        #         # gas = self.web3.eth.estimate_gas(transaction)
        #         # gas = int(gas * 1.5)  
        #         # transaction.update({'gas': gas})

        #     except (json.JSONDecodeError, FileNotFoundError) as e:
        #         logger.error(f"Error loading ABI: {str(e)}")
        #         raise ValueError(f"Error loading ABI: {str(e)}")

        # if transaction is not None:
        #     # Sign and send the transaction
        #     signed_tx = self.web3.eth.account.sign_transaction(transaction, self.private_key)
        #     tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            
        #     receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
        #     if receipt.status == 1:
        #         return tx_hash.hex()
        #     else:
        #         raise ValueError("Transaction failed")
        # else:
        #     raise ValueError("Failed to build transaction")
