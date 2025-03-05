from django import forms
from .models import CustomUser

class LoginForm(forms.Form):
    CATEGORY_CHOICES = [
        ('', 'Выберите должность'),
        ('nach_choices', 'Начальник'),
        ('fak_choices', 'Дежурный по факультету'),
        ('kaf_choices', 'Дежурный по кафедре'),
        ('kurs_choices', 'Дежурный по курсу'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True, label="Категория")
    subcategory = forms.ChoiceField(choices=[], required=True, label="Подкатегория")
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Загружаем подкатегории по умолчанию
        self.nach_choices = [(usr.id, usr.username) for usr in CustomUser.objects.filter(username__icontains="Начальник")]
        self.fak_choices = [(usr.id, usr.username) for usr in CustomUser.objects.filter(username__icontains="факультету")]
        self.kaf_choices = [(usr.id, usr.username) for usr in CustomUser.objects.filter(username__icontains="кафедре")]
        self.kurs_choices = [(usr.id, usr.username) for usr in CustomUser.objects.filter(username__icontains="курс")]

        # Если форма была отправлена, обновляем choices для subcategory
        if self.data:
            self.update_choices(self.data.get('category'))

    def update_choices(self, category):
        """Обновляет `choices` для `subcategory` в зависимости от категории"""
        categories = {
            "nach_choices": self.nach_choices,
            "fak_choices": self.fak_choices,
            "kaf_choices": self.kaf_choices,
            "kurs_choices": self.kurs_choices,
        }
        self.fields['subcategory'].choices = categories.get(category, [])