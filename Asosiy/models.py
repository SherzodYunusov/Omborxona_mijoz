from django.db import models
from userapp.models import *


class Mahsulot(models.Model):
    tanlov = (('dona', 'dona'), ('kg','kg'),
                 ('qop', 'qop'), ('blok','blok'))
    nom = models.CharField(max_length=100)
    brend = models.CharField(max_length=100)
    narx = models.IntegerField()
    miqdor = models.PositiveSmallIntegerField()
    olchov = models.CharField(max_length=30, choices=tanlov)
    sana = models.DateField()
    ombor1 = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom}, {self.brend}"

class Mijoz(models.Model):
    ism = models.CharField(max_length=30)
    nom = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    qarz = models.PositiveSmallIntegerField(default=0)
    ombor1 = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ism}, {self.nom}"

# Create your models here.
