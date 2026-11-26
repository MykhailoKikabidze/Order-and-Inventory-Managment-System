from django.db import models
from django.db.models.functions import Lower

UNIT_CHOICES = (
        ('kg', 'Kilogram'),
        ('litre', 'Litre'),
        ('metre', 'Metre'),
        ('each', 'Each')
    )

class Product(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    base_unit = models.CharField(max_length=10,
                                  choices=UNIT_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = (
            models.UniqueConstraint(Lower('sku'), name='unique_lower_sku_ci'),
            models.CheckConstraint(
                condition=models.Q(base_unit__in=[value for value, label in UNIT_CHOICES]),
                name='product_valid_base_unit'
            ),
            models.CheckConstraint(
                condition=~models.Q(sku__regex=r'^\s*$'),
                name='product_sku_not_empty',    
            ),
            models.CheckConstraint(
                condition=~models.Q(name__regex=r'^\s*$'),
                name='product_name_not_empty',
            ),
        )



