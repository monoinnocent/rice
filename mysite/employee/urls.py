from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('forgetpassword', views.forgetpassword, name='forgetpassword'),
    path('homedashboard', views.homedashboard, name='homedashboard'),
    path('user', views.user, name='user'),
    path('useredit', views.useredit, name='useredit'),
]
