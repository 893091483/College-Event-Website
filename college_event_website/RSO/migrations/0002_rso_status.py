# Generated by Django 3.1.6 on 2021-03-27 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSO', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rso',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
