# Generated by Django 3.0.3 on 2020-05-07 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_employee_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
