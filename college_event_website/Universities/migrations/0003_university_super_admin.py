# Generated by Django 3.1.6 on 2021-04-03 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Universities', '0002_auto_20210324_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='super_admin',
            field=models.IntegerField(null=True),
        ),
    ]