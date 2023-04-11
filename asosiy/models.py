from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Muallif(models.Model):
    j=[("erkak","erkak"),("ayol","ayol")]
    ism=models.CharField(max_length=50)
    jinsi=models.CharField(max_length=50,choices=j)
    t = [("ha", "ha"), ("yoq", "yoq")]
    tirik=models.CharField(max_length=50,choices=t)
    kitob_soni=models.SmallIntegerField()
    tugulgan_sana=models.DateField()
    def __str__(self):
        return self.ism
class Talaba(models.Model):
    b=[("ha","ha"),("yoq","yoq")]
    ism=models.CharField(max_length=50)
    bitiruvchi=models.CharField(max_length=50,choices=b)
    kitoblar_soni=models.PositiveIntegerField(default=0)
    kurs=models.PositiveIntegerField()
    def __str__(self):
        return self.ism
class Admin(models.Model):
    ism=models.CharField(max_length=50)
    ish_vaqti=models.TimeField()
    def __str__(self):
        return self.ism
class Kitob(models.Model):
    nom=models.CharField(max_length=100)
    sahifa=models.PositiveIntegerField()
    muallif=models.ForeignKey(Muallif,on_delete =models.CASCADE)
    janr=models.CharField(max_length=100)
    def __str__(self):
        return self.nom
class Record(models.Model):
    q=[("ha","ha"),("yoq","yoq")]
    talaba=models.ForeignKey(Talaba,on_delete=models.CASCADE)
    kitob=models.ForeignKey(Kitob,on_delete=models.CASCADE)
    admin=models.ForeignKey(Admin,on_delete=models.CASCADE)
    olingan_sana=models.DateField()
    qaytarish_sanasi=models.DateField()
    qaytardi=models.CharField(max_length=50,choices=q)
