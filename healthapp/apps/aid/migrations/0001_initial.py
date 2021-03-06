# Generated by Django 2.0.7 on 2020-08-10 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('name', models.CharField(max_length=32, verbose_name='疾病类别')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('name', models.CharField(max_length=32, verbose_name='药品')),
                ('drug_kind', models.SmallIntegerField(choices=[(0, '西药'), (1, '中成药'), (2, '其他类')], default=0, verbose_name='药品类别')),
                ('drug_otc', models.SmallIntegerField(choices=[(0, '处方药'), (1, 'OTC甲'), (2, 'OTC乙'), (3, '未知类别')], default=0, verbose_name='otc类别')),
                ('drug_yibao', models.SmallIntegerField(choices=[(0, '医保甲'), (1, '医保乙'), (2, '非医保'), (3, '未知类别')], default=0, verbose_name='医保类别')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Drugdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('general_name', models.CharField(max_length=32, verbose_name='药品学名')),
                ('commodity_name', models.CharField(max_length=32, verbose_name='药品俗名')),
                ('spell_name', models.CharField(max_length=32, verbose_name='药品拼音')),
                ('ingredient', models.IntegerField(choices=[(0, '西药'), (1, '中成药'), (2, '其他类')], verbose_name='药品类型')),
                ('prescription', models.IntegerField(choices=[(0, '处方药'), (1, 'OTC甲'), (2, 'OTC乙'), (3, '未知类别')], verbose_name='处方级别')),
                ('insurance', models.IntegerField(choices=[(0, '医保甲'), (1, '医保乙'), (2, '非医保'), (3, '未知类别')], verbose_name='医保类型')),
                ('disease', models.CharField(max_length=128, verbose_name='适用疾病')),
                ('dosage_form', models.CharField(max_length=32, verbose_name='药品剂型')),
                ('dosage', models.CharField(max_length=32, verbose_name='剂量')),
                ('_character', models.CharField(max_length=32, verbose_name='药品说明')),
                ('major_ingredient', models.CharField(max_length=32, verbose_name='主要成分')),
                ('auxiliary_ingredient', models.CharField(max_length=64, verbose_name='辅助药品')),
                ('for_symptom', models.TextField(verbose_name='适用疾病')),
                ('specification', models.CharField(max_length=32, verbose_name='规格')),
                ('poor_reactions', models.TextField(verbose_name='副作用')),
                ('_usage', models.CharField(max_length=32, verbose_name='用量')),
                ('congtraindicant', models.CharField(max_length=32, verbose_name='用药禁忌')),
                ('note', models.CharField(max_length=128, verbose_name='注意事项')),
                ('pregnant_note', models.CharField(max_length=128, verbose_name='孕妇须知')),
                ('children_note', models.CharField(max_length=128, verbose_name='儿童须知')),
                ('old_note', models.CharField(max_length=128, verbose_name='老年人须知')),
                ('drug_interactions', models.CharField(max_length=128, verbose_name='底部声明')),
                ('pharmacological', models.TextField(verbose_name='药理实验')),
                ('pharmacokinetics', models.CharField(max_length=128, verbose_name='')),
                ('store', models.CharField(max_length=32, verbose_name='存储方式')),
                ('period', models.CharField(max_length=32, verbose_name='保质期')),
                ('execution_standard', models.CharField(max_length=32, verbose_name='执行标准')),
                ('approval_numbers', models.CharField(max_length=32, verbose_name='国药准字号')),
                ('production_enterprises', models.CharField(max_length=32, verbose_name='制药企业')),
                ('picture', models.ImageField(default='drug/default.png', max_length=255, upload_to='drug', verbose_name='封面图片')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否展示')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('name', models.CharField(max_length=32, verbose_name='症状')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
