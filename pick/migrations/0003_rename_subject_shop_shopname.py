# Generated by Django 3.2.16 on 2023-01-07 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pick', '0002_rename_title_option_drinkname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='subject',
            new_name='shopname',
        ),
    ]
