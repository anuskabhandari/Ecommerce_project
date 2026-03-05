from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length =100)
    price = models.FloatField(default=0.0)  # ✅ default number
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True) 
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
