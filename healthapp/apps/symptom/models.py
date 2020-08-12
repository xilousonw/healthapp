from django.db import models

# Create your models here.
from healthapp.utils.models import BaseModel


class body(BaseModel):
    body_id = (
        (0,'body'),
        (1,'skin'),
        (2,'head'),
        (3,'chest'),
        (4,'stomach'),
        (5,'pelvis'),
        (6,'arm'),
        (7,'leg'),
    )
    name = models.IntegerField(choices=body_id,verbose_name='身体部位')

class organ(BaseModel):
    name = models.CharField(max_length=32,verbose_name='器官')

    body = models.ForeignKey(to='body',on_delete=models.CASCADE,verbose_name='对应部位')


class symptom(BaseModel):
    name = models.CharField(max_length=32,verbose_name='症状')

    organ = models.ForeignKey(to='organ',on_delete=models.CASCADE,verbose_name='对应器官')



