from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    position = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)


    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.username or '')  # или другое поле для отображения


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class CustomUserManager(models.Manager):
    def get_by_natural_key(self, username):
        return self.get(username=username)

objects = CustomUserManager()
DoesNotExist = models.Manager

class info(models.Model):
    customUser =  models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    personalInfo = models.CharField(max_length=255)

