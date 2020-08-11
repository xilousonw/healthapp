from django.db import models

# Create your models here.
from healthapp.utils.models import BaseModel


class disease(BaseModel):
    name = models.CharField(max_length=32,verbose_name='疾病名称')


class subject(BaseModel):
    name = models.CharField(max_length=32,verbose_name='疾病分类')
