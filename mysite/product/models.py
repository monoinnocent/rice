from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name_breed = models.CharField(max_length=45)
    type_breed = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'product'

class QualityControl(models.Model):
    quality_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quality_lot = models.IntegerField()
    quality_date = models.DateField()
    quality_keep_date = models.DateField()
    seed_moistness = models.FloatField()
    seed_germination = models.FloatField()
    seed_strong = models.FloatField()
    quality_weight = models.FloatField()
    quality_check_date = models.FloatField() 

    class Meta:
        managed = False
        db_table = 'quality_control'



