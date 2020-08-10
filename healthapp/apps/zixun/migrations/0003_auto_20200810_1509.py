# Generated by Django 2.0.7 on 2020-08-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zixun', '0002_auto_20200810_1008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news_detail',
            options={'verbose_name': '资讯详情', 'verbose_name_plural': '资讯详情'},
        ),
        migrations.RemoveField(
            model_name='news',
            name='zixun_img',
        ),
        migrations.AddField(
            model_name='news',
            name='news_img',
            field=models.ImageField(blank=True, default='icon/default.png', max_length=255, null=True, upload_to='courses', verbose_name='封面图片'),
        ),
        migrations.AddField(
            model_name='news_detail',
            name='news_detail_img',
            field=models.ImageField(blank=True, default='icon/default.png', max_length=255, null=True, upload_to='courses', verbose_name='封面图片'),
        ),
        migrations.AlterModelTable(
            name='news_detail',
            table='news_detail',
        ),
    ]