from django.db import models

class Kursy(models.Model):
    name_kurs = models.CharField(max_length=20)
    poSpisku = models.CharField(max_length=10)
    naLitso = models.CharField(max_length=10)
    naryad = models.CharField(max_length=10)
    bolnye = models.CharField(max_length=10)
    uvolnenie = models.CharField(max_length=10)
    otpusk = models.CharField(max_length=10)
    objects = models.Manager()
    DoesNotExist = models.Manager

    class Meta:
        verbose_name = 'Расход Курса'
        verbose_name_plural = 'Расход курсов'
