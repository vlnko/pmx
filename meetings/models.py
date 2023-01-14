from django.db import models
import datetime
from accounts.models import CustomUser


class Meeting(models.Model):
    title = models.CharField(max_length=16, blank=False)
    date = models.DateField(default=datetime.date.today, auto_now=False, auto_now_add=False, verbose_name='Дата проведения')
    created = models.DateField(verbose_name='Создан', auto_now_add=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    decision = models.TextField(verbose_name='Решения', blank=True)
    participators = models.ManyToManyField(CustomUser, related_name='participators', verbose_name='Участники')

    def __str__(self):
        return f'{self.title} - {self.date}'

    class Meta:
        verbose_name = 'Совещание'
        verbose_name_plural = 'Совещания'
