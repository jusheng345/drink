# Generated by Django 3.2.16 on 2023-01-07 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pick', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='title',
            new_name='drinkname',
        ),
    ]
