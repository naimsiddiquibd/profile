# Generated by Django 3.1 on 2021-04-29 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0006_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
