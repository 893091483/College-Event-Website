# Generated by Django 3.1.6 on 2021-03-27 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RSO', '0002_rso_status'),
        ('Events', '0009_auto_20210327_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='rso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RSO.rso'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.TimeField(default='13:54:36'),
        ),
    ]