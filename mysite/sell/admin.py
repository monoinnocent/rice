from django.contrib import admin

from .models import Customer, Sell, LineSell
# Register your models here.
admin.site.register(Customer)
admin.site.register(Sell)
admin.site.register(LineSell)

