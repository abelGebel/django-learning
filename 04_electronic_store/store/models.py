import os
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 200)
    price = models.FloatField()
    description = models.TextField(default="")
    image = models.ImageField(verbose_name="imagen del producto", upload_to="media/products")

    def __str__(self):
        return self.name
    
@receiver(post_delete, sender=Product)
def eliminar_imagen_producto(sender, instance, **kwargs):
    # Eliminar el archivo de imagen asociado al producto
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)