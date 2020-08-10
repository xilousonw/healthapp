from django.db import models

# Create your models here.
from healthapp.utils.models import BaseModel




class Firstaid(BaseModel):
    c_name = models.CharField(max_length=32, verbose_name='中文症状名')
    e_name = models.CharField(max_length=64, verbose_name='英文症状名')
    makecall = models.CharField(max_length=128, verbose_name='呼叫指导')
    do_steps = models.CharField(max_length=128, verbose_name='急救步骤')
    go_doctor = models.CharField(max_length=128, verbose_name='就医判断条件')
    # appreciation =models.CharField(max_length=32)
    remarks = models.BooleanField(default=False,verbose_name='是否收藏')
    # last_update_by = models.CharField(null=True,verbose_name='修改人')
    # last_update_time = models.DateTimeField(null=True,verbose_name='修改时间')
    class Meta:
        db_table = "firstaid"
        verbose_name = "急救知识"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.c_name

