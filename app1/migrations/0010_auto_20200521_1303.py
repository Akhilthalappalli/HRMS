# Generated by Django 3.0.3 on 2020-05-21 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_menumaster_rolepermission'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rolepermission',
            old_name='delete',
            new_name='delet',
        ),
    ]