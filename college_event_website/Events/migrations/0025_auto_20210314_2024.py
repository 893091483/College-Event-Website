# Generated by Django 3.1.6 on 2021-03-15 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0024_auto_20210314_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.TimeField(default='20:24:29'),
        ),
    ]
