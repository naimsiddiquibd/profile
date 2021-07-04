# Generated by Django 3.1 on 2021-05-08 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('button', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=150)),
                ('feature', models.FileField(upload_to='favicon/')),
                ('image', models.FileField(upload_to='favicon/')),
            ],
            options={
                'verbose_name': 'B. Add Items',
                'verbose_name_plural': 'B. Add Items',
            },
        ),
        migrations.AlterModelOptions(
            name='porthead',
            options={'verbose_name': 'A. Edit Title', 'verbose_name_plural': 'A. Edit Title'},
        ),
        migrations.AlterField(
            model_name='porthead',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]