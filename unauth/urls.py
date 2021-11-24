from django.urls import path, include
from . import views

app_name = "unauth"

urlpatterns = [
    path('', views.welcome, name = 'w_home'),
    path('login_btn_url', views.gotoLogin),
    path('register_btn_url', views.gotoRegister),
    path('register', views.register, name='register'),
    path('login', views.loginPage, name='login'),
]