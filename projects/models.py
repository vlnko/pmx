from django.db import models
import datetime, re
from accounts.models import CustomUser
from ckeditor.fields import RichTextField


class Project(models.Model):
    id = models.AutoField(verbose_name='ID проекта', primary_key=True)
    title = models.CharField(verbose_name='Наименование проекта', max_length=24, blank=False)
    category = models.CharField(verbose_name='Категория', max_length=48)
    description = RichTextField(verbose_name='Описание')
    created = models.DateField(verbose_name='Создан', auto_now_add=True)
    deadline = models.DateField(
        default=datetime.date.today, auto_now=False, auto_now_add=False, verbose_name='Дедлайн')
    head = models.ForeignKey(
        CustomUser, on_delete=models.DO_NOTHING, verbose_name='Руководитель', blank=True, null=True, related_name='proj_head')
    project_team = models.ManyToManyField(CustomUser, related_name='proj_team', verbose_name='Команда')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def days_remaining(self): # gets how many days remain to deadline
        d = str(self.deadline - datetime.date.today())[:-9]
        numbers = re.search(r'\d+', d)
        if numbers != None:
            numbers = numbers.group()
        else:
            numbers = 0
        num_days = int(numbers)
        words = ['день', 'дня', 'дней']
        if num_days % 10 == 1 and num_days % 100 != 11:
            p = 0
        elif 2 <= num_days % 10 <= 4 and (num_days % 100 < 10 or num_days % 100 >= 20):
            p = 1
        else:
            p = 2
        if self.deadline < datetime.date.today():
            return f'Просрочено на {num_days} {words[p]}'
        else:
            return f'Остается {num_days} {words[p]}'

    def progress(self): # gets percentage of tasks done in the project
        count_tasks_all = len(self.task_set.all())
        count_tasks_done = len(self.task_set.all().filter(status="ED"))
        if count_tasks_all > 0:
            percent = count_tasks_done / count_tasks_all * 100
            p = int(percent)
        else:
            p = 0
        return p
    
    def get_tasks(self): # gets all tasks related to the project
        tasks = self.task_set.all().order_by('status', 'date_end')
        return tasks
    

def one_week_from_today(): # this is used to set deadline automatically one week from today
    return datetime.datetime.now() + datetime.timedelta(days=7)


class Task(models.Model):
    class Status(models.TextChoices):
        AI = "AI", "Входящие"
        BW = "BW", "В работе"
        CC = "CC", "На проверке"
        DR = "DR", "Исправляется"
        ED = "ED", "Готово"
    
    id = models.AutoField(verbose_name='ID задачи', primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    title = models.CharField(verbose_name='Наименование задачи', max_length=100, blank=False)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.AI, verbose_name='Статус')
    description = RichTextField(verbose_name='Описание')
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
        if datetime.date.today() > self.date_end and self.status != "ED": # checking if task is late
            delta = str(datetime.date.today() - self.date_end)[:-9] # getting delta
            return f"{self.title} (late for {delta})"
        else:
            return self.title