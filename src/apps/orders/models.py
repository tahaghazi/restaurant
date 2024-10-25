from django.db import models
from src.apps.menus.models import MenuItem

# Create your models here.


class Order(models.Model):
    """Model for customer orders in the restaurant."""
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    table_number = models.IntegerField()  # Table number if it's a dine-in order
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.get_status_display()}"

    def total_cost(self):
        """Calculate the total cost of the order."""
        return sum(item.total_price() for item in self.order_items.all())


class OrderItem(models.Model):
    """Model for items within an order."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price per item at the time of order

    def __str__(self):
        return f"{self.menu_item.name} (x{self.quantity})"

    def total_price(self):
        """Calculate the total price for this item (quantity * price)."""
        return self.quantity * self.price
