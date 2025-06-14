from django.db import transaction
from web3 import Web3
from core.models import Order, Transactions, Item
import os

w3 = Web3(Web3.HTTPProvider(os.getenv("ETHEREUM_URL")))


def get_transaction_status(transaction_hash):
    print("get transaction status")
    tx_receipt = w3.eth.getTransactionReceipt(transaction_hash)
    print("receipt:", tx_receipt)
    if tx_receipt is None:
        return Order.MINT_NOT_STARTED
    elif tx_receipt['status'] == 1:
        return Order.MINT_SUCCEEDED
    else:
        return Order.MINT_FAILED


@transaction.atomic
def create_transaction_on_completed(order_id):
    try:
        order_instance = Order.objects.select_for_update().get(id=order_id)
        if not Transactions.objects.filter(order_id=order_id).exists():

            order_instance.delivered = True
            order_instance.save()

            tr = Transactions.objects.create(
                amount=order_instance.amount,
                quantity=order_instance.quantity,
                user_id=order_instance.user_id,
                text="internal payment method created transaction for ItemID:"
                     f" {order_instance.item_id}, quantity: {order_instance.quantity}, amount: {order_instance.amount}",
                blockchain_uuid=order_instance.blockchain_uuid,
                order_id=order_instance.id,
                object_type='v' if order_instance.item.type == Item.CREDIT_TOKEN else 'n'
            )

            return tr

        else:
            print(f"A transaction already exists for order with ID {order_instance.id}")
            return None
    except Exception as e:
        transaction.set_rollback(True)
        print(f"Error occurred while creating transaction: {e}")
        return None
