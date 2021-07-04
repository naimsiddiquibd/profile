# Generated by Django 3.2 on 2021-04-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0002_rename_settings_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='sm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'B. Social Media Link',
                'verbose_name_plural': 'B. Social Media Link',
            },
        ),
    ]