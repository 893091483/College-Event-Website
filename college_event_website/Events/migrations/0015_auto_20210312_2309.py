# Generated by Django 3.1.7 on 2021-03-13 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0014_auto_20210312_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.TimeField(default='23:09:12'),
        ),
    ]