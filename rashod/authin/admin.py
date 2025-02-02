from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'position','last_name']

@admin.register(CustomUser)
class YourUserAdmin(admin.ModelAdmin):
    form = CustomUserCreationForm

# Регистрация модели в админке
try:
    admin.site.register(CustomUser, YourUserAdmin)
except admin.sites.AlreadyRegistered:
    print("Модель CustomUser уже зарегистрирована.")

#Модели курсов в админке

