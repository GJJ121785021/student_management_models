# Generated by Django 2.2.7 on 2020-03-26 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0002_auto_20200327_0004'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='classinfo',
            table='ClassInfo',
        ),
        migrations.AlterModelTable(
            name='courseinfo',
            table='CourseInfo',
        ),
        migrations.AlterModelTable(
            name='scoreinfo',
            table='ScoreInfo',
        ),
        migrations.AlterModelTable(
            name='studentinfo',
            table='StudentInfo',
        ),
    ]