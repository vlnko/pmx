from django.db import models
import datetime, re
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

    def days_remaining(self):
        d = str(self.deadline - datetime.date.today())[:-9]
        numbers = re.search(r'\d+', d)
        if numbers != None:
            numbers = numbers.group()
        else:
            numbers = 0
        num_days = int(numbers)
        den = set((1, 21, 31, 41, 51, 61, 71, 81, 91, 101, 121, 131, 141, 151, 161, 171, 181, 191, 201))
        dna = set((2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94, 102, 103, 104, 122, 123, 124, 132, 133, 134, 142, 143, 144, 152, 153, 154, 162, 163, 164, 172, 173, 174, 182, 183, 184, 192, 193, 194, 202, 203, 204))
        if num_days in den:
            d = f'{ num_days } день'
        elif num_days in dna:
            d = f'{ num_days } дня'
        else:
            d = f'{ num_days } дней'
        return d

    def progress(self):
        count_tasks_all = len(self.task_set.all())
        count_tasks_done = len(self.task_set.all().filter(status="DN"))
        if count_tasks_all > 0:
            percent = count_tasks_done / count_tasks_all * 100
            p = int(percent)
        else:
            p = 0
        return p
    
    def get_tasks(self):
        tasks = self.task_set.all()
        return tasks


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