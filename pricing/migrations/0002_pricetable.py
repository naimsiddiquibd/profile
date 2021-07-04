# Generated by Django 3.2 on 2021-05-08 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pricetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=150)),
                ('offer1', models.TextField(blank=True, max_length=150, null=True)),
                ('offer2', models.TextField(blank=True, max_length=150, null=True)),
                ('offer3', models.TextField(blank=True, max_length=150, null=True)),
                ('offer4', models.TextField(blank=True, max_length=150, null=True)),
                ('offer5', models.TextField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'A. Edit Title',
                'verbose_name_plural': 'A. Edit Title',
            },
        ),
    ]