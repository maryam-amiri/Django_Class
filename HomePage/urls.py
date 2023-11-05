from django.urls import path

from . import views

app_name='HomePage'

urlpatterns=[
    path('',views.HomePage,name='home'),
    path('HomePage.html',views.HomePage,name='HomePage'),
    path('register.html', views.register, name='register'),
    path('login.html', views.user_login, name='login'),
    path('reg_buy', views.register_buy, name='reg_buy'),
    path('logout.html', views.HomePage, name='user_logout'),
]