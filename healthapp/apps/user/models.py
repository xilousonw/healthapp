from django.db import models

from django.contrib.auth.models import AbstractUser
from healthapp.utils.models import BaseModel

from uuid import uuid4
import time
def create_userid():
    str1 = uuid4()
    str2 = time.time()



class User(AbstractUser):

    uid = models.CharField(create_userid())
    telephone = models.CharField(max_length=11,verbose_name='手机号')
    icon = models.ImageField(upload_to='icon', default='icon/default.png')
    # auth模块的user自带email字段了
    # email = models.EmailField(verbose_name='邮箱')



class UseInfo(AbstractUser):


    uid = models.OneToOneField(to='User',on_delete=models.CASCADE,verbose_name='用户一对一外键')

    sex = models.IntegerField(choices=((0,'男'),(1,'女')),verbose_name='性别')
    birthday = models.DateTimeField(verbose_name='生日')
    location = models.CharField(max_length=32,verbose_name='所在位置(城市)')
    wechat = models.CharField(max_length=32,verbose_name='微信号')
    weibo = models.CharField(max_length=32,verbose_name='微博')
    qq = models.CharField(max_length=16,verbose_name='QQ号')
    level = models.IntegerField(verbose_name='用户等级')
    coin = models.IntegerField(verbose_name='用户代币数')


    class Meta:
        db_table = "UserInfo"
        verbose_name = "用户详情"
        verbose_name_plural = verbose_name


    def sex_cn(self):
        # 返回性别
        return self.get_sex_display()

# class UserInfo(BaseModel):

