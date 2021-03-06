# Generated by Django 3.2 on 2021-04-29 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('image', models.FileField(upload_to='services/')),
                ('color', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'B. Items',
                'verbose_name_plural': 'B. Items',
            },
        ),
    ]
