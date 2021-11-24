from django.db import models
from django.contrib.auth.models import User

parts = (('1/2', '50%'),
         ('1/3', '33%'),
         ('1/4', '25%'),
         ('Full', '100%'))

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Исполнитель')
    identified = models.TextField('Идентификатор')
    in_wait_status = models.BooleanField(verbose_name='В ожидании')
    manager = models.TextField('Менеджер')
    short_description = models.TextField(verbose_name='Короткое описание')
    full_description = models.TextField(verbose_name='Полное описание')
    deadline = models.DateField('Дедлайн')
    payment = models.IntegerField('Цена')
    status = models.TextField('Статус')
    documentation_link = models.TextField('Ссылка на методички')
    project_link = models.TextField('Ссылка на проект')
    payment_parts = models.CharField(max_length=50, choices=parts, default='1/2', verbose_name='Части оплаты')
    part1 = models.BooleanField('Первая часть оплачена')
    part2 = models.BooleanField('Вторая часть оплачена')
    part3 = models.BooleanField('Третья часть оплачена')
    part4 = models.BooleanField('Четвёртая часть оплачена')

    def __str__(self):
        return self.identified

    class Meta:
        verbose_name = 'Таск'
        verbose_name_plural = 'Таски'

class payment_mdl(models.Model):
    task_fk = models.ForeignKey(Task, verbose_name='Таск', on_delete=models.CASCADE,)
    payment_id = models.TextField('Идентификатор оплаты')
    summa = models.IntegerField('Сумма')
    payment_date = models.DateField('Дата поступления оплаты')
    paid = models.BooleanField(verbose_name='Оплачено?',default=False)

    def __str__(self):
        return self.payment_id

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'