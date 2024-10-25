from django.db import models

# Create your models here.

class Ingredient(models.Model):
    """Basic model for each ingredient in the inventory."""
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20, default="pcs")  # e.g., "kg", "liters", "pcs"
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Total quantity in stock

    def __str__(self):
        return self.name