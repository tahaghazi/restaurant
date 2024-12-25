from rest_framework import viewsets

from .serializers import OrderSerializer, OrderItemSerializer
from ..models import Order, OrderItem


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return OrderItem.objects.filter(user=self.request.user, ordered=False)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    new = False

    def get_object(self):
        if not self.new:
            return super().get_object()
        # Get or create the order
        obj = Order.objects.get_or_create(user=self.request.user, ordered=False)[0]

        # Get all order items for the user where ordered=False
        order_items = OrderItem.objects.filter(user=self.request.user, ordered=False)

        # Iterate through each unique menu item and consolidate quantities
        for item in order_items:
            # Find all items with the same menu item name and not ordered
            matching_items = order_items.filter(menu_item__name=item.menu_item.name, ordered=False)

            if matching_items.count() > 1:
                print(f"Found duplicates for {item.menu_item.name}")

                # Get the first item in the group (this will be the "main" item)
                main_item = matching_items.first()

                # Add the quantity of the current item to the main item
                main_item.quantity += item.quantity
                print(f"Updated quantity for {main_item.menu_item.name}: {main_item.quantity}")

                # Save the updated main item
                main_item.save()

                # Delete all other redundant items in the group
                for redundant_item in matching_items[1:]:
                    redundant_item.delete()

        # Refresh order_items after deletion to ensure the order items list is up to date
        order_items = OrderItem.objects.filter(user=self.request.user, ordered=False)

        # Associate all order items with the order and save
        obj.order_items.set(order_items)
        obj.save()
        return obj

    def list(self, request, *args, **kwargs):
        self.new = True
        return super().retrieve(request, *args, **kwargs)
