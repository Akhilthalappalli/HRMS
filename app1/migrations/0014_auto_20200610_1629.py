# Generated by Django 3.0.3 on 2020-06-10 10:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_auto_20200601_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 10, 16, 29, 40, 654296)),
        ),
    ]