from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import  CustomUser

users = CustomUser.objects.all()
class LoginForm(forms.Form):
    selection = forms.ChoiceField(
        choices=[(usr.id, str(usr)) for usr in users],
        label='Должность:',
        required=True
    )

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)

