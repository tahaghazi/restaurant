from django.contrib.auth import get_user_model
from django.db import models

from src.apps.menus.models import MenuItem


# Create your models here.


class OrderItem(models.Model):
    """Model for items within an order."""
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price per item at the time of order
    ordered = models.BooleanField(default=False)  # Has the order been placed?
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='carts', blank=True, null=True)

    def __str__(self):
        return f"{self.menu_item.name} (x{self.quantity})"

    def save(self, *args, **kwargs):
        """Override the save method to update the price of the item."""
        self.price = self.menu_item.price * self.quantity
        super().save(*args, **kwargs)

    def total_price(self):
        """Calculate the total price for this item (quantity * price)."""
        return self.quantity * self.price

class Order(models.Model):
    """Model for customer orders in the config."""
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    table_number = models.IntegerField(null=True, blank=True)  # Table number if it's a dine-in order
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField(default=False)  # Has the order been placed?
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders', blank=True, null=True)
    order_items = models.ManyToManyField(OrderItem, related_name='cart', blank=True, null=True)

    def __str__(self):
        return f"Order #{self.id} - {self.get_status_display()}"

    def total_cost(self):
        """Calculate the total cost of the order."""
        return sum(item.total_price() for item in self.order_items.all())

    def save(self, *args, **kwargs):
        if self.status == 'COMPLETED':
            self.ordered = True
            self.order_items.all().update(ordered=True)
        super().save(*args, **kwargs)

