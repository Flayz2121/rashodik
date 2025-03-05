from django.contrib import admin
from .models import Kursy, naryads, bolnyes, uvolnenies, otpusks

@admin.register(Kursy)
class KursyAdmin(admin.ModelAdmin):
    list_display = ('name_kurs', 'poSpisku', 'naLitso', 'naryad', 'bolnye', 'uvolnenie', 'otpusk','fakultet')


    def naryad(self, obj):
        return ', '.join([str(n) for n in obj.naryads.all()])

    def bolnye(self, obj):
        return ', '.join([str(b) for b in obj.bolnyes.all()])

    def uvolnenie(self, obj):
        return str(obj.uvolnenies.first())

    def otpusk(self, obj):
        return str(obj.otpusks.first())

@admin.register(naryads)
class NaryadsAdmin(admin.ModelAdmin):
    list_display = ('Kursy_id','information_of_naryads_1','information_of_naryads_2','information_of_naryads_3','information_of_naryads_4'
                    ,'information_of_naryads_5','information_of_naryads_6','information_of_naryads_7','information_of_naryads_8'
                    ,'information_of_naryads_9','information_of_naryads_10','information_of_naryads_11','information_of_naryads_12'
                    ,'information_of_naryads_13','information_of_naryads_14','information_of_naryads_15','information_of_naryads_16'
                    ,'information_of_naryads_17','information_of_naryads_18','information_of_naryads_19','information_of_naryads_20'
                    ,'information_of_naryads_21','information_of_naryads_22','information_of_naryads_23','information_of_naryads_24'
                    ,'information_of_naryads_25','information_of_naryads_26','information_of_naryads_27','information_of_naryads_28'
                    ,'information_of_naryads_29','information_of_naryads_30','information_of_naryads_31','information_of_naryads_32'
                    ,'information_of_naryads_33','information_of_naryads_34','information_of_naryads_35','information_of_naryads_36'
                    ,'information_of_naryads_37','information_of_naryads_38','information_of_naryads_39','information_of_naryads_40')

@admin.register(bolnyes)
class BolnyesAdmin(admin.ModelAdmin):
    list_display = ('Kursy_id','information_of_bolnyes_1','information_of_bolnyes_2','information_of_bolnyes_3','information_of_bolnyes_4',
                    'information_of_bolnyes_5','information_of_bolnyes_6','information_of_bolnyes_7','information_of_bolnyes_8',
                    'information_of_bolnyes_9','information_of_bolnyes_10','information_of_bolnyes_11','information_of_bolnyes_12',
                    'information_of_bolnyes_13','information_of_bolnyes_14','information_of_bolnyes_15','information_of_bolnyes_16',
                    'information_of_bolnyes_17','information_of_bolnyes_18','information_of_bolnyes_19','information_of_bolnyes_20'
                    ,'information_of_bolnyes_21','information_of_bolnyes_22','information_of_bolnyes_23','information_of_bolnyes_24'
                    ,'information_of_bolnyes_25','information_of_bolnyes_26','information_of_bolnyes_27','information_of_bolnyes_28'
                    ,'information_of_bolnyes_29','information_of_bolnyes_30','information_of_bolnyes_31','information_of_bolnyes_32'
                    ,'information_of_bolnyes_33','information_of_bolnyes_34','information_of_bolnyes_35','information_of_bolnyes_36'
                    ,'information_of_bolnyes_37','information_of_bolnyes_38','information_of_bolnyes_39','information_of_bolnyes_40')

@admin.register(uvolnenies)
class UvolneniesAdmin(admin.ModelAdmin):
    list_display = ('Kursy_id','information_of_uvolnenies_1','information_of_uvolnenies_2','information_of_uvolnenies_3','information_of_uvolnenies_4'
                    ,'information_of_uvolnenies_5','information_of_uvolnenies_6','information_of_uvolnenies_7','information_of_uvolnenies_8'
                    ,'information_of_uvolnenies_9','information_of_uvolnenies_10','information_of_uvolnenies_11','information_of_uvolnenies_12'
                    ,'information_of_uvolnenies_13','information_of_uvolnenies_14','information_of_uvolnenies_15','information_of_uvolnenies_16'
                    ,'information_of_uvolnenies_17','information_of_uvolnenies_18','information_of_uvolnenies_19','information_of_uvolnenies_20'
                    ,'information_of_uvolnenies_21','information_of_uvolnenies_22','information_of_uvolnenies_23','information_of_uvolnenies_24'
                    ,'information_of_uvolnenies_25','information_of_uvolnenies_26','information_of_uvolnenies_27','information_of_uvolnenies_28'
                    ,'information_of_uvolnenies_29','information_of_uvolnenies_30','information_of_uvolnenies_31','information_of_uvolnenies_32'
                    ,'information_of_uvolnenies_33','information_of_uvolnenies_34','information_of_uvolnenies_35','information_of_uvolnenies_36'
                    ,'information_of_uvolnenies_37','information_of_uvolnenies_38','information_of_uvolnenies_39','information_of_uvolnenies_40')

@admin.register(otpusks)
class OtpusksAdmin(admin.ModelAdmin):
    list_display = ('Kursy_id','information_of_otpusks_1','information_of_otpusks_2','information_of_otpusks_3','information_of_otpusks_4'
                    ,'information_of_otpusks_5','information_of_otpusks_6','information_of_otpusks_7','information_of_otpusks_8'
                    ,'information_of_otpusks_9','information_of_otpusks_10','information_of_otpusks_11','information_of_otpusks_12'
                    ,'information_of_otpusks_13','information_of_otpusks_14','information_of_otpusks_15','information_of_otpusks_16'
                    ,'information_of_otpusks_17','information_of_otpusks_18','information_of_otpusks_19','information_of_otpusks_20'
                    ,'information_of_otpusks_21','information_of_otpusks_22','information_of_otpusks_23','information_of_otpusks_24'
                    ,'information_of_otpusks_25','information_of_otpusks_26','information_of_otpusks_27','information_of_otpusks_28'
                    ,'information_of_otpusks_29','information_of_otpusks_30','information_of_otpusks_31','information_of_otpusks_32'
                    ,'information_of_otpusks_33','information_of_otpusks_34','information_of_otpusks_35','information_of_otpusks_36'
                    ,'information_of_otpusks_37','information_of_otpusks_38','information_of_otpusks_39','information_of_otpusks_40')
