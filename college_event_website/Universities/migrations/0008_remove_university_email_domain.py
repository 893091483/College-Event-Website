# Generated by Django 3.1.6 on 2021-03-15 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Universities', '0007_auto_20210314_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='email_domain',
        ),
    ]
