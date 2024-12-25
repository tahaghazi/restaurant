from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import MenuItemSerializer
from ..models import MenuItem


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ['get', 'options', 'head']
