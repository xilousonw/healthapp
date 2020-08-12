from django.db import models

# Create your models here.
from healthapp.utils.models import BaseModel


class accompany(BaseModel):
    accompany_type  = (
        (0,'普通陪诊'),
        (1,'儿童陪诊'),
        (2,'孕妇陪诊'),
        (3,'老人陪诊'),
    )
    # accompany = models.IntegerField(choices=)