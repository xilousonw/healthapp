# Generated by Django 2.0.7 on 2020-08-13 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aid', '0003_auto_20200813_1037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drug',
            options={'verbose_name': '药品简介', 'verbose_name_plural': '药品简介'},
        ),
        migrations.AlterModelTable(
            name='drug',
            table='drug',
        ),
    ]
