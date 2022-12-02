from django.db import models
import datetime
from accounts.models import CustomUser


class Project(models.Model):
    id = models.AutoField(verbose_name='ID проекта', primary_key=True)
    title = models.CharField(verbose_name='Наименование проекта', max_length=50, blank=False)
    category = models.CharField(verbose_name='Категория', max_length=50)
    description = models.TextField(verbose_name='Описание')
    created = models.DateField(verbose_name='Создан', auto_now_add=True)
    deadline = models.DateField(default=datetime.date.today, auto_now=False, auto_now_add=False, verbose_name='Дедлайн')
    head = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, verbose_name='Руководитель', blank=True, null=True)

    def __str__(self):
        return self.title + ' (created ' + str(self.created) + ')'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


def one_week_from_today():
    return datetime.datetime.now() + datetime.timedelta(days=7)


class Task(models.Model):
    class Status(models.TextChoices):
        IN = "IN", "INBOX"
        WO = "WO", "WORKING"
        CK = "CK", "CHECKING"
        RW = "RW", "REWORKING"
        DN = "DN", "DONE"
    
    id = models.AutoField(verbose_name='ID задачи', primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    title = models.CharField(verbose_name='Наименование задачи', max_length=100, blank=False)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.IN, verbose_name='Статус')
    description = models.TextField(verbose_name='Описание')
    created = models.DateField(verbose_name='Создан', auto_now_add=True)
    date_start = models.DateField(default=datetime.date.today, auto_now=False, auto_now_add=False, verbose_name='Дата начала')
    date_end = models.DateField(default=one_week_from_today, auto_now=False, auto_now_add=False, verbose_name='Дата окончания')
 
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        if datetime.date.today() > self.date_end and self.status != "DN":
            delta = str(datetime.date.today() - self.date_end)[:-9]
            return self.title + ' (late for ' + delta + ')'
        else:
            return self.title

    def is_late(self):
        if datetime.datetime.now() > self.date_end and self.is_done == False:
            return True
        else:
            return False
    
    def is_done(self):
        if self.status == "DN":
            return True