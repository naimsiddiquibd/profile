# Generated by Django 3.2 on 2021-05-20 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_auto_20210520_2106'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='messages',
            new_name='txtmessages',
        ),
    ]
