import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


# Sample User model
class Product(models.Model):
    UPC = models.CharField(max_length=5, default=00000)
    Name = models.CharField(max_length=50, default="Cheese")
    Price = models.FloatField(default=0.0)

def __str__(self):
        return f"{self.Name} ({self.UPC})"
    
