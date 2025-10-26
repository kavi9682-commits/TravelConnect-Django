from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Destination(models.Model):
    name= models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    description= models.TextField()
    image = models.ImageField(upload_to='destinations/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.destination.name}"