from django.db import models

# Create your models here.

class Products(models.Model):

    CATEGORIES = (
        ('Food', 'Food'),
        ('Clothes', 'Clothes'),
        ('Other', 'Other')
    )

    name = models.CharField(max_length=100)
    quantity = models.PositiveBigIntegerField()
    category = models.CharField(max_length=100, choices=CATEGORIES, default='Food')

    def __str__(self):
        return f'{self.name} ({self.category}): {self.quantity}'
