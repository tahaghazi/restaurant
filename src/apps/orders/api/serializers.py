from .utils import BaseSaveSerializer
from ..models import Order, OrderItem
from ...menus.api.serializers import MenuItemSerializer


class OrderItemSerializer(BaseSaveSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"
        read_only_fields = ("order", "price", "ordered", "user")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["menu_item"] = MenuItemSerializer(instance.menu_item).data
        return data


class OrderSerializer(BaseSaveSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at", "ordered", "order_items")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["total_cost"] = instance.total_cost()
        return data
