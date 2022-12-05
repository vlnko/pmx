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
    head = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, verbose_name='Руководитель', blank=True, null=True, related_name='proj_head')
    project_team = models.ManyToManyField(CustomUser, related_name='proj_team', verbose_name='Команда')

    def __str__(self):
        return f"{self.title} (created {self.created})"

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def days_remaining():
        delta = str(self.date_end - datetime.date.today())[:-9]
        return delta


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
    executor = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, verbose_name='Исполнитель')
    work_hours_plan = models.IntegerField(verbose_name='Часы (план)', default=1)
    work_hours_fact = models.IntegerField(verbose_name='Часы (факт)', default=1)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        if datetime.date.today() > self.date_end and self.status != "DN":
            delta = str(datetime.date.today() - self.date_end)[:-9]
            return f"{self.title} (late for {delta})"
        else:
            return self.title

    def is_late(self):
        if datetime.datetime.now() > self.date_end and self.status != "DN":
            return True
        else:
            return False