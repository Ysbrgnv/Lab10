# Generated by Django 3.0.4 on 2020-04-17 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200417_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='salary',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
