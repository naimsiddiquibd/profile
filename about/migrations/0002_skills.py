# Generated by Django 3.2 on 2021-04-29 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=150)),
                ('rate', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'B. Skills',
                'verbose_name_plural': 'B. Skills',
            },
        ),
    ]
