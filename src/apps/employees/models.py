from django.db import models

# Create your models here.

class Employee(models.Model):
    """Model for config employees."""
    ROLE_CHOICES = [
        ('MANAGER', 'Manager'),
        ('CHEF', 'Chef'),
        ('WAITER', 'Waiter'),
        ('CASHIER', 'Cashier'),
        ('HOST', 'Host'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)  # Unique email for each employee
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)  # Track if the employee is currently active
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)  # Base salary for the employee
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Additional bonus or compensation

    def total_salary(self):
        """Calculate the total salary including base salary and bonus."""
        return self.base_salary + self.bonus

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"


class Schedule(models.Model):
    """Model for employee work schedules."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    notes = models.TextField(blank=True, null=True)  # Additional notes for the schedule

    def __str__(self):
        return f"{self.employee} - {self.date} ({self.start_time} to {self.end_time})"
