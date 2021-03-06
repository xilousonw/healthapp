# Generated by Django 2.0.7 on 2020-08-12 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0004_auto_20200812_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='accompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('accompany', models.IntegerField(choices=[(0, '普通陪诊'), (1, '儿童陪诊'), (2, '孕妇陪诊'), (3, '老人陪诊')], verbose_name='陪诊类型')),
                ('serve_time_gap', models.CharField(max_length=32, verbose_name='服务时间段')),
                ('serve_process', models.CharField(max_length=32, verbose_name='服务流程')),
                ('serve_content', models.TextField(verbose_name='服务内容')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('ap_time', models.DateTimeField(verbose_name='预约时间')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='陪诊费用')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('name', models.CharField(max_length=32, verbose_name='名字')),
                ('district', models.CharField(max_length=128, verbose_name='所属区')),
                ('level', models.IntegerField(choices=[(0, '三甲'), (1, '三级'), (2, '二级'), (3, '社区')], verbose_name='医院级别')),
                ('address', models.CharField(max_length=128, verbose_name='医院具体地址')),
            ],
            options={
                'verbose_name': '医院',
                'verbose_name_plural': '医院',
                'db_table': 'hospital',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150, verbose_name='订单标题')),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='订单总价')),
                ('out_trade_no', models.CharField(max_length=64, unique=True, verbose_name='订单号')),
                ('trade_no', models.CharField(max_length=64, null=True, verbose_name='流水号')),
                ('order_status', models.SmallIntegerField(choices=[(0, '未支付'), (1, '已支付'), (2, '已取消'), (3, '超时取消')], default=0, verbose_name='订单状态')),
                ('pay_type', models.SmallIntegerField(choices=[(1, '支付宝'), (2, '微信支付')], default=1, verbose_name='支付方式')),
                ('pay_time', models.DateTimeField(null=True, verbose_name='支付时间')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_user', to='user.User', verbose_name='下单用户')),
            ],
            options={
                'verbose_name': '订单记录',
                'verbose_name_plural': '订单记录',
                'db_table': 'accompany_order',
            },
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('name', models.CharField(max_length=32, verbose_name='就诊人姓名')),
                ('sex', models.IntegerField(choices=[(0, '男'), (1, '女')], verbose_name='性别')),
                ('telephone', models.CharField(max_length=11, verbose_name='手机号')),
                ('id_num', models.CharField(max_length=18, verbose_name='身份证')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='appointment',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accompany.hospital', verbose_name='医院'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accompany.patient', verbose_name='就诊人'),
        ),
    ]
