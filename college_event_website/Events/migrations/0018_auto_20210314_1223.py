# Generated by Django 3.1.6 on 2021-03-14 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0017_auto_20210314_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.TimeField(default='12:23:38'),
        ),
    ]
