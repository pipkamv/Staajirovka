from django.db import models
from django.contrib.auth.models import AbstractUser


class ProfileUser(AbstractUser):
    patronymic = models.CharField(max_length=25, blank=True,  verbose_name='Отчество')
    phone_number = models.CharField(max_length=12, blank=True, verbose_name='Номер телефона', default='0312000000')
    address = models.CharField(max_length=100, blank=True, verbose_name='Адрес')
    inn = models.CharField(max_length=14, blank=True, verbose_name='ИНН', default='000000000000')

    def __str__(self):
        return f'Профиль пользователя {self.username}'

    class Meta(AbstractUser.Meta):
        verbose_name = 'Ползователь'
        verbose_name_plural = 'Пользователи'

