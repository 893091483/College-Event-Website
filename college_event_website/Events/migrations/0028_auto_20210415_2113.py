# Generated by Django 3.1.6 on 2021-04-16 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0027_auto_20210415_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default='2021-13-04/15/21 21:13:07', null=True),
        ),
    ]
