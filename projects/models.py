from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.AutoField(verbose_name='ID проекта', primary_key=True)
    title = models.CharField(verbose_name='Наименование проекта', max_length=50)
    description = models.TextField(verbose_name='Описание')
    created = models.DateField(verbose_name='Создан', auto_now_add=True)

    def __str__(self):
        return self.title + ' (created ' + str(self.created) + ')'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'