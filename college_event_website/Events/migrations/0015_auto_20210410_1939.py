# Generated by Django 3.1.6 on 2021-04-10 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0014_auto_20210404_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.TimeField(default='19:39:55'),
        ),
    ]
