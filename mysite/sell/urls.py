from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('selldatatables', views.selldatatables, name='selldatatables'),
    path('sellcreate', views.sellcreate, name='sellcreate'),
    path('sellview', views.sellview, name='sellview'),
    path('sellviewcreate', views.sellviewcreate, name='sellviewcreate'),
    path('sellviewdata', views.sellviewdata, name='sellviewdata'),
    path('sellviewedit', views.sellviewedit, name='sellviewedit'),

    path('selltimeseries', views.selltimeseries, name='selltimeseries'),

]
