# Generated by Django 3.1.6 on 2021-04-15 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0025_auto_20210415_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
