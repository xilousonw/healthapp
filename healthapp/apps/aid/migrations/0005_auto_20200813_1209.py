# Generated by Django 2.0.7 on 2020-08-13 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aid', '0004_auto_20200813_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drugdetail',
            options={'verbose_name': '药品详情', 'verbose_name_plural': '药品详情'},
        ),
        migrations.AlterModelTable(
            name='drugdetail',
            table='drugdetail',
        ),
    ]
