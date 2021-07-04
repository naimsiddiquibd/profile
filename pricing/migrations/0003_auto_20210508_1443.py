# Generated by Django 3.2 on 2021-05-08 08:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0002_pricetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricetable',
            name='button',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pricetable',
            name='link',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pricetable',
            name='price',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pricetable',
            name='icon',
            field=models.FileField(upload_to='prices/'),
        ),
        migrations.AlterField(
            model_name='pricetable',
            name='offer1',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='pricetable',
            name='offer2',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='pricetable',
            name='offer3',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='pricetable',
            name='offer4',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='pricetable',
            name='offer5',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
