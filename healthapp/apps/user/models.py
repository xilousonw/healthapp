from django.db import models

from django.contrib.auth.models import AbstractUser
from healthapp.utils.models import BaseModel

class User(AbstractUser):
    telephone = models.CharField(max_length=11,verbose_name='手机号')
    icon = models.ImageField(upload_to='icon', default='icon/default.png')
    # email = models.EmailField(verbose_name='邮箱')
    # wechat = models.CharField(max_length=32,verbose_name='微信号')
    # weibo = models.CharField(max_length=32,verbose_name='微博号')
    # qq = models.CharField(max_length=16,verbose_name='qq号')
    # level = models.IntegerField(null=True,verbose_name='等级')
    # coin = models.IntegerField(null=True,verbose_name='代币数')
    # sex = models.IntegerField(choices=((0,'男'),(1,'女')),verbose_name='性别')
    # birthday = models.DateTimeField(null=True,verbose_name='生日')
    # location = models.CharField(null=True,max_length=32,verbose_name='所在位置(城市)')


# class UserInfo(BaseModel):

