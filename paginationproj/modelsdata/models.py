from django.db import models

# Create your models here.
class ItemList(models.Model):
    name = models.CharField(max_length=40)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
        