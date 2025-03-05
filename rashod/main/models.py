from django.db import models

class Kursy(models.Model):
    name_kurs = models.CharField(primary_key=True,max_length=20)
    poSpisku = models.IntegerField(default=0)
    naLitso = models.IntegerField(default=0)
    naryad = models.IntegerField(default=0)
    bolnye = models.IntegerField(default=0)
    uvolnenie = models.IntegerField(default=0)
    otpusk = models.IntegerField(default=0)
    fakultet = models.CharField(max_length=20)
    objects = models.Manager()
    DoesNotExist = models.Manager

    class Meta:
        verbose_name = 'Расход Курса'
        verbose_name_plural = 'а-Расход курсов'
        ordering = ['name_kurs']

class naryads(models.Model):
    Kursy =  models.ForeignKey(Kursy, on_delete=models.CASCADE,related_name='naryads', null=True, blank=True)
    information_of_naryads_1 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_1_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_1_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_2 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_2_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_2_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_3 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_3_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_3_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_4 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_4_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_4_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_5 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_5_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_5_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_6 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_6_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_6_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_7 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_7_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_7_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_8 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_8_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_8_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_9 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_9_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_9_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_10 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_10_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_10_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_11 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_11_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_11_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_12 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_12_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_12_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_13 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_13_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_13_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_14 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_14_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_14_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_15 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_15_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_15_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_16 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_16_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_16_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_17 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_17_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_17_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_18 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_18_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_18_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_19 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_19_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_19_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_20 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_20_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_20_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_21 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_21_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_21_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_22 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_22_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_22_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_23 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_23_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_23_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_24 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_24_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_24_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_25 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_25_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_25_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_26 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_26_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_26_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_27 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_27_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_27_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_28 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_28_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_28_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_29 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_29_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_29_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_30 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_30_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_30_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_31 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_31_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_31_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_32 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_32_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_32_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_33 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_33_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_33_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_34 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_34_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_34_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_35 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_35_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_35_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_36 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_36_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_36_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_37 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_37_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_37_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_38 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_38_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_38_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_39 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_39_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_39_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_naryads_40 = models.CharField(max_length=20, null=True, blank=True)
    info_of_naryads_40_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_naryads_40_vremya = models.CharField(max_length=30, null=True, blank=True)
    objects = models.Manager()


    class Meta:
        verbose_name = 'Наряды Курса'
        verbose_name_plural = 'Наряды курсов'


class bolnyes(models.Model):
    Kursy =  models.ForeignKey(Kursy,max_length=20, on_delete=models.CASCADE, related_name='bolnyes',to_field='name_kurs', null=True, blank=True)
    information_of_bolnyes_1 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_1_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_1_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_2 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_2_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_2_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_3 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_3_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_3_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_4 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_4_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_4_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_5 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_5_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_5_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_6 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_6_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_6_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_7 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_7_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_7_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_8 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_8_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_8_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_9 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_9_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_9_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_10 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_10_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_10_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_11 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_11_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_11_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_12 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_12_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_12_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_13 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_13_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_13_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_14 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_14_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_14_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_15 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_15_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_15_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_16 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_16_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_16_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_17 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_17_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_17_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_18 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_18_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_18_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_19 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_19_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_19_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_20 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_20_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_20_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_21 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_21_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_21_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_22 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_22_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_22_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_23 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_23_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_23_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_24 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_24_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_24_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_25 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_25_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_25_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_26 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_26_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_26_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_27 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_27_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_27_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_28 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_28_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_28_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_29 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_29_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_29_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_30 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_30_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_30_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_31 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_31_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_31_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_32 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_32_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_32_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_33 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_33_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_33_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_34 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_34_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_34_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_35 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_35_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_35_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_36 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_36_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_36_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_37 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_37_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_37_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_38 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_38_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_38_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_39 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_39_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_39_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_bolnyes_40 = models.CharField(max_length=20, null=True, blank=True)
    info_of_bolnyes_40_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_bolnyes_40_vremya = models.CharField(max_length=30, null=True, blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Больные Курса'
        verbose_name_plural = 'Больные курсов'



class uvolnenies(models.Model):
    Kursy =  models.ForeignKey(Kursy, on_delete=models.CASCADE, related_name='uvolnenies', null=True, blank=True)
    information_of_uvolnenies_1 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_1_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_1_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_2 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_2_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_2_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_3 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_3_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_3_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_4 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_4_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_4_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_5 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_5_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_5_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_6 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_6_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_6_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_7 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_7_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_7_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_8 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_8_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_8_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_9 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_9_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_9_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_10 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_10_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_10_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_11 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_11_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_11_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_12 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_12_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_12_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_13 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_13_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_13_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_14 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_14_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_14_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_15 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_15_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_15_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_16 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_16_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_16_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_17 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_17_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_17_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_18 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_18_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_18_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_19 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_19_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_19_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_20 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_20_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_20_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_21 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_21_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_21_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_22 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_22_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_22_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_23 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_23_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_23_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_24 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_24_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_24_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_25 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_25_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_25_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_26 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_26_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_26_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_27 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_27_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_27_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_28 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_28_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_28_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_29 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_29_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_29_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_30 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_30_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_30_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_31 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_31_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_31_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_32 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_32_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_32_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_33 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_33_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_33_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_34 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_34_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_34_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_35 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_35_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_35_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_36 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_36_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_36_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_37 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_37_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_37_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_38 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_38_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_38_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_39 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_39_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_39_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_uvolnenies_40 = models.CharField(max_length=20, null=True, blank=True)
    info_of_uvolnenies_40_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_uvolnenies_40_vremya = models.CharField(max_length=30, null=True, blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Увольняемые Курса'
        verbose_name_plural = 'Увольняемые курсов'



class otpusks(models.Model):
    Kursy =  models.ForeignKey(Kursy, on_delete=models.CASCADE, related_name='otpusks', null=True, blank=True)
    information_of_otpusks_1 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_1_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_1_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_2 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_2_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_2_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_3 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_3_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_3_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_4 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_4_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_4_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_5 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_5_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_5_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_6 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_6_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_6_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_7 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_7_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_7_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_8 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_8_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_8_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_9 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_9_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_9_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_10 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_10_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_10_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_11 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_11_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_11_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_12 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_12_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_12_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_13 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_13_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_13_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_14 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_14_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_14_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_15 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_15_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_15_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_16 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_16_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_16_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_17 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_17_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_17_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_18 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_18_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_18_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_19 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_19_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_19_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_20 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_20_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_20_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_21 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_21_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_21_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_22 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_22_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_22_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_23 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_23_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_23_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_24 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_24_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_24_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_25 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_25_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_25_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_26 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_26_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_26_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_27 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_27_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_27_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_28 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_28_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_28_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_29 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_29_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_29_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_30 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_30_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_30_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_31 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_31_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_31_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_32 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_32_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_32_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_33 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_33_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_33_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_34 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_34_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_34_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_35 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_35_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_35_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_36 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_36_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_36_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_37 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_37_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_37_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_38 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_38_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_38_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_39 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_39_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_39_vremya = models.CharField(max_length=30, null=True, blank=True)

    information_of_otpusks_40 = models.CharField(max_length=20, null=True, blank=True)
    info_of_otpusks_40_mesto = models.CharField(max_length=30, null=True, blank=True)
    info_of_otpusks_40_vremya = models.CharField(max_length=30, null=True, blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Отпуск Курса'
        verbose_name_plural = 'Отпуск курсов'


