from django.db import models

class TelegramUser(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ім\'я користувача в телеграмі')
    surname = models.CharField(max_length=100, verbose_name='Прізвище користувача в телеграмі')
    username = models.CharField(max_length=100, verbose_name='Юзернейм користувача в телеграмі')
    telegram_id = models.CharField(max_length=100, verbose_name='Айді користувача в телеграмі')
    questioned_name = models.CharField(max_length=100, verbose_name='Ім\'я користувача з анкети')
    sex = models.CharField(max_length=100, verbose_name='Стать користувача в телеграмі') # TODO: maybe do as choice field

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return f'@{self.username}'
