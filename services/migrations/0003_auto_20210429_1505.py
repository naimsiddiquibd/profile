# Generated by Django 3.2 on 2021-04-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='description',
            new_name='link',
        ),
        migrations.AddField(
            model_name='items',
            name='subtitle',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
