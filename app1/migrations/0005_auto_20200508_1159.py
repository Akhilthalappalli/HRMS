# Generated by Django 3.0.3 on 2020-05-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_employee_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='course',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='institute',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='mark',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='yoc',
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
    ]
