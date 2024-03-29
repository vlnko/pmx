# Generated by Django 4.1.1 on 2023-01-14 18:41

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата проведения')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Создан')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('decision', models.TextField(blank=True, verbose_name='Решения')),
                ('participators', models.ManyToManyField(related_name='participators', to=settings.AUTH_USER_MODEL, verbose_name='Участники')),
            ],
            options={
                'verbose_name': 'Совещание',
                'verbose_name_plural': 'Совещания',
            },
        ),
    ]
