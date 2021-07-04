# Generated by Django 3.2 on 2021-05-20 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=250)),
                ('messages', models.TextField(max_length=750)),
            ],
            options={
                'verbose_name': 'A. Chech Emails',
                'verbose_name_plural': 'A. Chech Emails',
            },
        ),
    ]