# Generated by Django 3.1 on 2021-04-29 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0004_hireme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='hireme',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sm',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
