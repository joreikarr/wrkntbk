# Generated by Django 3.2.7 on 2021-09-27 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identified', models.TextField(verbose_name='Идентификатор')),
                ('in_wait_status', models.BooleanField(verbose_name='В ожидании')),
                ('manager', models.TextField(verbose_name='Менеджер')),
                ('short_description', models.CharField(max_length=100, verbose_name='Короткое описание')),
                ('full_description', models.CharField(max_length=500, verbose_name='Полное описание')),
                ('deadline', models.DateField(verbose_name='Дедлайн')),
                ('payment', models.IntegerField(verbose_name='Цена')),
                ('status', models.TextField(verbose_name='Статус')),
                ('documentation_link', models.TextField(verbose_name='Ссылка на методички')),
                ('project_link', models.TextField(verbose_name='Ссылка на проект')),
                ('payment_parts', models.CharField(choices=[('1/2', '50%'), ('1/3', '33%'), ('1/4', '25%'), ('Full', '100%')], default='1/2', max_length=50)),
                ('part1', models.BooleanField(verbose_name='Первая часть оплачена')),
                ('part2', models.BooleanField(verbose_name='Вторая часть оплачена')),
                ('part3', models.BooleanField(verbose_name='Третья часть оплачена')),
                ('part4', models.BooleanField(verbose_name='Четвёртая часть оплачена')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель')),
            ],
        ),
    ]
