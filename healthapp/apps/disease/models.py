from django.db import models

# Create your models here.
from healthapp.utils.models import BaseModel


class disease(BaseModel):
    title = models.CharField(max_length=32,verbose_name='疾病学科')
    e_name = models.CharField(max_length=32,verbose_name='英文名')
    name = models.CharField(max_length=32,verbose_name='中文名')
    alias = models.CharField(max_length=32,verbose_name='别名')
    description = models.CharField(max_length=128, verbose_name='描述')
    expect = models.CharField(max_length=128, verbose_name='患者须知')
    how_common = models.CharField(max_length=128,verbose_name='流行病学统计')
    risk_factors = models.CharField(max_length=128,null=True,verbose_name='危险因素')
    treatment = models.CharField(max_length=128,verbose_name='治疗方法')
    self_care = models.CharField(max_length=128,verbose_name='自我诊疗')




class subject(BaseModel):
    name = models.CharField(max_length=32,verbose_name='疾病分类')
