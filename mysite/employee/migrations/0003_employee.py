# Generated by Django 2.2.1 on 2019-05-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20190520_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_username', models.CharField(max_length=45)),
                ('emp_password', models.CharField(max_length=45)),
                ('emp_firstname', models.CharField(max_length=45)),
                ('emp_lastname', models.CharField(max_length=45)),
                ('emp_phone', models.CharField(max_length=45)),
                ('emp_email', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
    ]
