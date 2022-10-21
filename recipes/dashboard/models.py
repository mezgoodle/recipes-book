from tabnanny import verbose
from django.db import models

class TelegramUser(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ім\'я користувача в телеграмі')
    surname = models.CharField(max_length=100, verbose_name='Прізвище користувача в телеграмі')
    username = models.CharField(max_length=100, verbose_name='Юзернейм користувача в телеграмі')
    telegram_id = models.CharField(max_length=100, verbose_name='Айді користувача в телеграмі')
    questioned_name = models.CharField(max_length=100, verbose_name='Ім\'я користувача з анкети')
    sex = models.CharField(max_length=100, verbose_name='Стать користувача в телеграмі')

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return f'@{self.username}'


class Recipe(models.Model):
    name = models.CharField(max_length=20, verbose_name='Назва рецепту')
    description = models.CharField(max_length=100, verbose_name='Опис рецепту')
    photo = models.ImageField(upload_to ='uploads/', verbose_name='Фото рецепту')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепти'

    def __str__(self):
        return f'@{self.name}'


class State(models.Model):
    telegram_id = models.CharField(max_length=20, verbose_name='Айді користувача в телеграмі')
    state = models.CharField(max_length=20, verbose_name='Стан користувача')
