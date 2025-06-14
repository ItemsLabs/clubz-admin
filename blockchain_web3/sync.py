from core.models import Order
from .utils import get_transaction_status, create_transaction_on_completed


def update_order_statuses():
    print("Running check and update order statuses")
    orders = Order.objects.filter(blockchain_order_status=Order.MINT_IN_PROGRESS).filter(delivered=False).filter(
        payment_platform_status=Order.COMPLETED)

    for order in orders:
        old_status = order.blockchain_order_status
        new_status = get_transaction_status(order.blockchain_uuid)
        print("old:", old_status, "new:", new_status)
        if new_status != old_status:
            order.blockchain_order_status = new_status
            order.save()
            if order.blockchain_order_status == Order.MINT_SUCCEEDED and not order.delivered:
                create_transaction_on_completed(order.id)
