from django.db import models
from product.models import Product

class Customer(models.Model):
    cus_id = models.AutoField(primary_key=True)
    cus_name = models.CharField(max_length=45)
    cus_address = models.CharField(max_length=45)
    cus_phone = models.CharField(max_length=45)
    cus_list = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'customer'

class Sell(models.Model):
    sell_id = models.AutoField(primary_key=True)
    sell_sum_amount = models.FloatField()
    sell_sum_price = models.FloatField()
    discount = models.IntegerField()
    discount_price = models.FloatField()
    sell_total_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'sell'

class LineSell(models.Model):
    line_sell_id = models.AutoField(primary_key=True)
    sell = models.ForeignKey(Sell, on_delete=models.CASCADE)
    cus = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sell_amount = models.IntegerField()
    sell_breed_price = models.FloatField()
    sell_full_price = models.FloatField()
    sell_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'line_sell'