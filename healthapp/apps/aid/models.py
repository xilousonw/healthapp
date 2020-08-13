from django.db import models

# Create your models here.

from healthapp.utils.models import BaseModel


class Aid(BaseModel):
    name = models.CharField(max_length=32,verbose_name='疾病类别')


class Symptom(BaseModel):
    name = models.CharField(max_length=32,verbose_name='症状')

    aid = models.ForeignKey(to='Aid',on_delete=models.CASCADE,verbose_name='对应疾病类型')


class Drug(BaseModel):
    kind=(
        (0,'西药'),
        (1,'中成药'),
        (2,'其他类')
    )
    otc = (
        (0,'处方药'),
        (1,'OTC甲'),
        (2,'OTC乙'),
        (3,'未知类别')
    )
    yibao = (
        (0,'医保甲'),
        (1,'医保乙'),
        (2,'非医保'),
        (3,'未知类别')
    )
    name =models.CharField(max_length=32,verbose_name='药品')
    drug_kind = models.SmallIntegerField(choices=kind, default=0, verbose_name="药品类别")
    drug_otc = models.SmallIntegerField(choices=otc, default=0, verbose_name="otc类别")
    drug_yibao = models.SmallIntegerField(choices=yibao, default=0, verbose_name="医保类别")

    symptom = models.ForeignKey(to='Symptom', on_delete=models.DO_NOTHING, verbose_name='对应症状')

    company = models.ForeignKey(to='Company', on_delete=models.DO_NOTHING, verbose_name='对应制药公司')


class Drugdetail(BaseModel):
    ingredient_label = (
        (0, '西药'),
        (1, '中成药'),
        (2, '其他类')
    )
    prescription_label = (
        (0, '处方药'),
        (1, 'OTC甲'),
        (2, 'OTC乙'),
        (3, '未知类别')
    )
    insurance_label = (
        (0, '医保甲'),
        (1, '医保乙'),
        (2, '非医保'),
        (3, '未知类别')
    )
    general_name =models.CharField(max_length=32,verbose_name='药品学名')
    commodity_name =models.CharField(max_length=32,verbose_name='药品俗名')
    spell_name =models.CharField(max_length=32,verbose_name='药品拼音')
    ingredient = models.IntegerField(choices=ingredient_label,verbose_name='药品类型')
    prescription = models.IntegerField(choices=prescription_label,verbose_name='处方级别')
    insurance = models.IntegerField(choices=insurance_label,verbose_name='医保类型')
    disease = models.CharField(max_length=128,verbose_name='适用疾病')
    dosage_form = models.CharField(max_length=32,verbose_name='药品剂型')
    dosage = models.CharField(max_length=32,verbose_name='剂量')
    _character = models.CharField(max_length=32,verbose_name='药品说明')
    major_ingredient = models.CharField(max_length=32,verbose_name='主要成分')
    auxiliary_ingredient = models.CharField(max_length=64,verbose_name='辅助药品')
    for_symptom = models.TextField(verbose_name='适用疾病')
    specification = models.CharField(max_length=32,verbose_name='规格')
    poor_reactions = models.TextField(verbose_name='副作用')
    _usage = models.CharField(max_length=32,verbose_name='用量')
    congtraindicant = models.CharField(max_length=32,verbose_name='用药禁忌')
    note = models.CharField(max_length=128,verbose_name='注意事项')
    pregnant_note = models.CharField(max_length=128,verbose_name='孕妇须知')
    children_note = models.CharField(max_length=128,verbose_name='儿童须知')
    old_note = models.CharField(max_length=128,verbose_name='老年人须知')
    drug_interactions = models.CharField(max_length=128,verbose_name='底部声明')
    pharmacological = models.TextField(verbose_name='药理实验')
    pharmacokinetics = models.CharField(max_length=128,verbose_name='药物代谢动力学')
    store = models.CharField(max_length=32,verbose_name='存储方式')
    period = models.CharField(max_length=32,verbose_name='保质期')
    execution_standard = models.CharField(max_length=32,verbose_name='执行标准')
    approval_numbers = models.CharField(max_length=32,verbose_name='国药准字号')
    production_enterprises = models.CharField(max_length=32,verbose_name='制药企业')
    # avg_score = models
    picture = models.ImageField(upload_to="drug", max_length=255, verbose_name="封面图片", default='drug/default.png')

class Company(BaseModel):
    name = models.CharField(max_length=32)
