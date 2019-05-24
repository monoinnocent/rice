from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buydatatables', views.buydatatables, name='buydatatables'),
    path('buycreate', views.buycreate, name='buycreate'),
    path('buyview', views.buyview, name='buyview'),
    path('buyedit', views.buyedit, name='buyedit'),
    path('supdatatables', views.supdatatables, name='supdatatables'),
    path('supview', views.supview, name='supview'),
    path('supedit', views.supedit, name='supedit'),
]
