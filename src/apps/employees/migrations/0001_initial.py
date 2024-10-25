# Generated by Django 4.2.16 on 2024-10-25 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("MANAGER", "Manager"),
                            ("CHEF", "Chef"),
                            ("WAITER", "Waiter"),
                            ("CASHIER", "Cashier"),
                            ("HOST", "Host"),
                        ],
                        max_length=20,
                    ),
                ),
                ("phone", models.CharField(blank=True, max_length=15, null=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("hire_date", models.DateField()),
                ("is_active", models.BooleanField(default=True)),
                ("base_salary", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "bonus",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schedules",
                        to="employees.employee",
                    ),
                ),
            ],
        ),
    ]
