# Generated by Django 3.2 on 2021-04-27 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0005_auto_20210427_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'C. Menu',
                'verbose_name_plural': 'C. Menu',
            },
        ),
    ]
