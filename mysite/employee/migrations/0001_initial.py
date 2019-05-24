# Generated by Django 2.2.1 on 2019-05-20 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=45)),
                ('explain', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'role',
            },
        ),
    ]
