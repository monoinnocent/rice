from django.db import models
from product.models import Product

class Supplier(models.Model):
    sup_id = models.AutoField(primary_key=True)
    sup_firstname = models.CharField(max_length=45)
    sup_lastname = models.CharField(max_length=45)
    sup_sex = models.CharField(max_length=45)
    sup_address = models.CharField(max_length=45)
    sup_field = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'supplier'

class Buy(models.Model):
    buy_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sup = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    buy_date = models.DateField()
    buy_weight = models.IntegerField()
    buy_moistness = models.FloatField()
    buy_moistness_cut = models.IntegerField()
    buy_adultrant_seed = models.FloatField()
    buy_adultrant_cut = models.IntegerField()
    buy_other_seed = models.IntegerField()
    buy_iodine = models.IntegerField()
    buy_redrice = models.IntegerField()
    buy_grade = models.CharField(max_length=2)
    buy_total_weight = models.IntegerField()
    buy_cost = models.FloatField()
    buy_total_cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'buy'
