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

    def get_object(self):
        obj = Order.objects.get_or_create(user=self.request.user, ordered=False)[0]
        order_items = OrderItem.objects.filter(user=self.request.user, ordered=False)
        obj.order_items.set(item.id for item in order_items)
        obj.save()
        return obj

    def list(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
