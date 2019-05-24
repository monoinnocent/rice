from django.db import models

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=45)  
    explain = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'role'

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    emp_username = models.CharField(max_length=45)
    emp_password = models.CharField(max_length=45)
    emp_firstname = models.CharField(max_length=45)
    emp_lastname = models.CharField(max_length=45)
    emp_phone = models.CharField(max_length=45)
    emp_email = models.CharField(max_length=45)
   
    class Meta:
        managed = False
        db_table = 'employee'

