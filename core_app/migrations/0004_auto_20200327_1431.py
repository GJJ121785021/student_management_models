# Generated by Django 2.2.7 on 2020-03-27 06:31

import core_app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0003_auto_20200327_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='classNum',
            field=core_app.models.MyTinyintField(verbose_name='班级人数'),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='courseHour',
            field=core_app.models.MyTinyintField(verbose_name='课时数'),
        ),
    ]
