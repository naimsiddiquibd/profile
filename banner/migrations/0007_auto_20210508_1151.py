# Generated by Django 3.1 on 2021-05-08 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0006_auto_20210429_1317'),
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
