from django.db import models
from django.contrib.auth.models import User


class Ombor(models.Model):
    nom = models.CharField(max_length=50)
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    manzil = models.CharField(max_length=50)
    soha = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ism}, {self.nom}"

# Create your models here.
