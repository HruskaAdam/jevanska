from django.db import models

class Apartment(models.Model):
    title = models.CharField(max_length=200)
    disposition = models.CharField(max_length=10)
    area = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='apartments/', blank=True, null=True)

    def __str__(self):
        return self.title