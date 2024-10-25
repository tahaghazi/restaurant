from django.db import models

# Create your models here.

class Table(models.Model):
    """Model for restaurant tables."""
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()  # Number of seats at the table
    is_available = models.BooleanField(default=True)  # Track if the table is available

    def __str__(self):
        return f"Table {self.table_number} - Capacity: {self.capacity}"


class Booking(models.Model):
    """Model for customer bookings or reservations."""
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    ]

    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    customer_email = models.EmailField(blank=True, null=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, related_name='bookings')
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    party_size = models.IntegerField()  # Number of people in the booking
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.customer_name} on {self.date} at {self.time}"

    def is_confirmed(self):
        """Check if the booking is confirmed."""
        return self.status == 'CONFIRMED'
