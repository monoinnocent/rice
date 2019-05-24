# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Buy(models.Model):
    buy_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField(blank=True, null=True)
    sup_id = models.IntegerField(blank=True, null=True)
    buy_date = models.DateField(blank=True, null=True)
    buy_weight = models.IntegerField(blank=True, null=True)
    buy_moistness = models.FloatField(blank=True, null=True)
    buy_moistness_cut = models.IntegerField(blank=True, null=True)
    buy_adultrant_seed = models.FloatField(blank=True, null=True)
    buy_adultrant_cut = models.IntegerField(blank=True, null=True)
    buy_other_seed = models.IntegerField(blank=True, null=True)
    buy_iodine = models.IntegerField(blank=True, null=True)
    buy_redrice = models.IntegerField(blank=True, null=True)
    buy_grade = models.CharField(max_length=2, blank=True, null=True)
    buy_total_weight = models.IntegerField(blank=True, null=True)
    buy_cost = models.FloatField(blank=True, null=True)
    buy_total_cost = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buy'


class Customer(models.Model):
    cus_id = models.AutoField(primary_key=True)
    cus_name = models.CharField(max_length=45, blank=True, null=True)
    cus_address = models.CharField(max_length=45, blank=True, null=True)
    cus_phone = models.CharField(max_length=45, blank=True, null=True)
    cus_list = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    role_id = models.IntegerField(blank=True, null=True)
    emp_username = models.CharField(max_length=45, blank=True, null=True)
    emp_password = models.CharField(max_length=45, blank=True, null=True)
    emp_firstname = models.CharField(max_length=45, blank=True, null=True)
    emp_lastname = models.CharField(max_length=45, blank=True, null=True)
    emp_phone = models.CharField(max_length=45, blank=True, null=True)
    emp_email = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class LineSell(models.Model):
    line_sell_id = models.IntegerField(primary_key=True)
    sell_id = models.IntegerField(blank=True, null=True)
    cus_id = models.IntegerField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    sell_amount = models.IntegerField(blank=True, null=True)
    sell_breed_price = models.FloatField(blank=True, null=True)
    sell_full_price = models.FloatField(blank=True, null=True)
    sell_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'line_sell'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name_breed = models.CharField(max_length=45, blank=True, null=True)
    type_breed = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class QualityControl(models.Model):
    quality_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField(blank=True, null=True)
    quality_lot = models.IntegerField(blank=True, null=True)
    quality_date = models.DateField(blank=True, null=True)
    quality_keep_date = models.DateField(blank=True, null=True)
    seed_moistness = models.FloatField(blank=True, null=True)
    seed_germination = models.FloatField(blank=True, null=True)
    seed_strong = models.FloatField(blank=True, null=True)
    quality_weight = models.FloatField(blank=True, null=True)
    quality_check_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quality_control'


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=45, blank=True, null=True)
    explain = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role'


class Sell(models.Model):
    sell_id = models.AutoField(primary_key=True)
    sell_sum_amount = models.FloatField(blank=True, null=True)
    sell_sum_price = models.FloatField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    discount_price = models.FloatField(blank=True, null=True)
    sell_total_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sell'


class Supplier(models.Model):
    sup_id = models.AutoField(primary_key=True)
    sup_firstname = models.CharField(max_length=45, blank=True, null=True)
    sup_lastname = models.CharField(max_length=45, blank=True, null=True)
    sup_sex = models.CharField(max_length=45, blank=True, null=True)
    sup_address = models.CharField(max_length=45, blank=True, null=True)
    sup_field = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'
