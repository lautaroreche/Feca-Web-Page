from django.db import models
from cloudinary.models import CloudinaryField


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image', resource_type='image')
    category = models.CharField(
        max_length=20,
        choices=[
            ('Cafe', 'Cafe'),
            ('Panaderia', 'Panaderia'),
            ('Comida', 'Comida'),
            ('Bebida', 'Bebida'),
            ('Otro', 'Otro'),
        ]
    )
