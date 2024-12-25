from .utils import BaseSaveSerializer
from ..models import Order, OrderItem


class OrderItemSerializer(BaseSaveSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
        read_only_fields = ("order", "price", "ordered", "user")


class OrderSerializer(BaseSaveSerializer):
    orders = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at", "ordered", "orders")
