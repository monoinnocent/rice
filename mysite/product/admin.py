from django.contrib import admin

from .models import Product, QualityControl
# Register your models here.
admin.site.register(Product)
admin.site.register(QualityControl)
