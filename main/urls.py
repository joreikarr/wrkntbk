from django.urls import path, include
from . import views
app_name = "main"
urlpatterns = [
    path('', views.index, name = 'index'),
    path('logout/', views.logoutUser, name='logout'),
    path('opened/', views.openedTasks, name='opened'),
    path('closed/', views.closedTasks, name='closed'),
    path('marks/', views.marksTasks, name='marks'),
    path('payments/', views.payments, name='payments'),
    path('new_task/', views.newTask, name='new_task'),
    path('frozen/', views.frozen, name='frozen'),
    path('setStatus/<str:id>/<str:status_n>', views.setStatus, name='setStatus'),
    path('setInWaitStatus/<str:id>/<status_n>', views.setInWaitStatus, name='setInWaitStatus'),
    path('setPayment/<str:id>/<int:payment_num>/<sum>/<divider>', views.setPayment, name='setPayment'),
    path('payment_page/<payment>', views.paymentPage, name = 'payment_page'),
    path('setPaymentStatus/<payment>/<status>', views.setPaymentStatus, name='setPaymentStatus'),
    path('task/<str:id>', views.taskPage, name='task'),
]