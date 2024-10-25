from django.db import models

# Create your models here.

# menus/models.py

class CuisineCategory(models.Model):
    """Model for cuisine categories, like 'Appetizers', 'Main Course', 'Desserts'."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    """Model for individual dishes or menu items."""
    name = models.CharField(max_length=100)
    category = models.ForeignKey(CuisineCategory, on_delete=models.CASCADE, related_name='menu_items')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price per item
    available = models.BooleanField(default=True)  # Is the item available for ordering?

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    """Model to link ingredients with menu items."""
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='ingredients')
    ingredient_name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)  # Simple text for quantity, e.g., '200g', '1 tsp'

    def __str__(self):
        return f"{self.ingredient_name} in {self.menu_item.name}"
