import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Task, payment_mdl
from .forms import CreateNewTask
from django import forms
from datetime import date, timedelta, datetime
from django.db.models import Q

days = ['Пн', 'Вт',
        'Ср', 'Чт',
        'Пт', 'Сб',
        'Вс']

months = ['Январь', 'Февраль', 'Март',
          'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь',
          'Октябрь', 'Ноябрь', 'Декабрь', ]


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        dates = calendar()
        dates_d = [x.strftime('%d') for x in dates]
        days_d = [days[x.weekday()] for x in dates]
        month = months[int(dates[0].strftime('%m')) - 1]
        tasks = []
        for dt in dates:
            temp_task = []
            temp_task = Task.objects.filter(deadline=dt, status='Активен', in_wait_status=False) | Task.objects.filter(
                deadline=dt, status='Правки', in_wait_status=False)
            temp_str = ''
            if len(temp_task) > 0:
                for t in temp_task:
                    temp_str +=  str(t.identified) + ', '
            tasks.append(temp_str)
        context = {'dates': dates_d, 'days': days_d, 'month': month, 'tasks': tasks}
        return render(request, 'main/index.html', context)
    else:
        return redirect('unauth:w_home')


def logoutUser(request):
    logout(request)
    return redirect('unauth:w_home')


def openedTasks(request):
    openedTasks_list = Task.objects.filter(status='Активен', in_wait_status=False)
    context = {'list': openedTasks_list}
    return render(request, 'main/opened.html', context)


def marksTasks(request):
    marksTasks_list = Task.objects.filter(status='Правки', in_wait_status=False)
    context = {'list': marksTasks_list}
    return render(request, 'main/marks.html', context)


def frozen(request):
    frozenTasks_list = Task.objects.filter(in_wait_status=True)
    context = {'list': frozenTasks_list}
    return render(request, 'main/wait.html', context)


def closedTasks(request):
    closedTasks_list = Task.objects.filter(status='Закрыт')
    context = {'list': closedTasks_list}
    return render(request, 'main/closed.html', context)


def payments(request):
    payments_list = payment_mdl.objects.all()
    unpaid_list = payment_mdl.objects.filter(paid=False)
    unpaid = 0
    if len(unpaid_list) > 0:
        for el in unpaid_list:
            unpaid += el.summa
    context = {'list': list(reversed(payments_list)), 'unpaid': unpaid}
    return render(request, 'main/payments.html', context)


def newTask(request):
    form = CreateNewTask(initial={'in_wait_status': False})
    if request.method == "POST":
        form = CreateNewTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    context = {'form': form}
    return render(request, 'main/new_task.html', context)


def taskPage(request, id):
    task = Task.objects.filter(identified=id)
    context = {'task': task[0]}
    return render(request, 'main/task_page.html', context)


def setStatus(request, id, status_n):
    Task.objects.filter(identified=id).update(status=status_n)
    task = Task.objects.filter(identified=id)
    context = {'task': task[0]}
    return render(request, 'main/task_page.html', context)


def setInWaitStatus(request, id, status_n):
    Task.objects.filter(identified=id).update(in_wait_status=status_n)
    task = Task.objects.filter(identified=id)
    context = {'task': task[0]}
    return render(request, 'main/task_page.html', context)


def setPayment(request, id, payment_num, sum, divider):
    if payment_num == 1:
        Task.objects.filter(identified=id).update(part1=True)
    elif payment_num == 2:
        Task.objects.filter(identified=id).update(part2=True)
    elif payment_num == 3:
        Task.objects.filter(identified=id).update(part3=True)
    elif payment_num == 4:
        Task.objects.filter(identified=id).update(part4=True)
    task = Task.objects.filter(identified=id)
    context = {'task': task[0]}
    sm = int(sum) / int(divider)
    pay_date = datetime.date.today()
    pid = str(task[0].identified) + ' ' + str(pay_date.strftime('%d.%m.%Y'))
    n_payment = payment_mdl(payment_id=pid, task_fk=task[0], summa=sm, payment_date=pay_date)
    n_payment.save()
    return render(request, 'main/task_page.html', context)


def setPaymentStatus(request, payment, status):
    cr_payment = payment_mdl.objects.filter(payment_id=payment)
    cr_payment.update(paid=status)
    context = {'payment': cr_payment[0]}
    return render(request, 'main/payment_page.html', context)


def paymentPage(request, payment):
    cr_payment = payment_mdl.objects.filter(payment_id=payment)
    context = {'payment': cr_payment[0]}
    calendar()
    return render(request, 'main/payment_page.html', context)


def calendar():
    m = datetime.now().month
    y = datetime.now().year
    ndays = (date(y, m + 1, 1) - date(y, m, 1)).days
    d1 = date(y, m, 1)
    d2 = date(y, m, ndays)
    delta = d2 - d1
    return ([(d1 + timedelta(days=i)) for i in range(delta.days + 1)])
