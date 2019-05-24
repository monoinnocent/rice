from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.index, name='index'),
    path('forgetpassword', views.forgetpassword, name='forgetpassword'),
    path('user', views.user, name='user'),
    path('useredit', views.useredit, name='useredit'),

    path('employee/', include('django.contrib.auth.urls')),
    
]

