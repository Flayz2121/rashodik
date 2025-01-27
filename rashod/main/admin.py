from django.contrib import admin
from .models import Kursy

class KursyAdmin(admin.ModelAdmin):
    list_display = ('name_kurs', 'poSpisku', 'naLitso', 'naryad', 'bolnye', 'uvolnenie','otpusk')


    # Регистрация модели в админке
try:
    admin.site.register( Kursy, KursyAdmin)
except admin.sites.AlreadyRegistered:
    print("Модель Kursy уже зарегистрирована.")
