from django.db import models
from Asosiy.models import Mahsulot, Mijoz
from userapp.models import Ombor
class Statistika(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    sana = models.DateTimeField(auto_created=True)
    miqdor = models.PositiveSmallIntegerField()
    umumiy_summa = models.PositiveSmallIntegerField()
    tolandi = models.PositiveSmallIntegerField()
    nasiya = models.PositiveSmallIntegerField()
    def sava(self, *args, **kwargs):
        self.umumiy_summa =int(self.miqdor) * int(self.mahsulot.narx)
        self.nasiya = self.umumiy_summa - int(self.tolandi)
        super(Statistika, self).save(*args, **kwargs)
# Create your models here.
