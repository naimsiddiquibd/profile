# Generated by Django 3.2 on 2021-04-27 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0004_auto_20210427_1509'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logo',
            options={'verbose_name': 'B. Change Logo', 'verbose_name_plural': 'B. Change Logo'},
        ),
        migrations.RenameField(
            model_name='logo',
            old_name='favicon',
            new_name='logo',
        ),
    ]
