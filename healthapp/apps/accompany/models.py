from django.db import models

# Create your models here.
from healthapp.utils.models import BaseModel
from user.models import User


class accompany(BaseModel):
    accompany_type  = (
        (0,'普通陪诊'),
        (1,'儿童陪诊'),
        (2,'孕妇陪诊'),
        (3,'老人陪诊'),
    )
    accompany = models.IntegerField(choices=accompany_type,verbose_name='陪诊类型')
    serve_time_gap = models.CharField(max_length=32,verbose_name='服务时间段')
    serve_process = models.CharField(max_length=32,verbose_name='服务流程')
    serve_content = models.TextField(verbose_name='服务内容')

    class Meta:
        db_table = "accompany"
        verbose_name = "陪诊"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.accompany

    @property
    def accompany_name(self):
        return self.get_accompany_display()


class appointment(BaseModel):

    ap_time = models.DateTimeField(verbose_name='预约时间')
    # patient = models.CharField(verbose_name='就诊人')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="陪诊费用", default=0)

    patient = models.ForeignKey(to='patient', on_delete=models.DO_NOTHING, verbose_name='就诊人')
    hospital = models.ForeignKey(to='hospital', on_delete=models.DO_NOTHING, verbose_name='医院')


class patient(BaseModel):
    name = models.CharField(max_length=32,verbose_name='就诊人姓名')
    sex = models.IntegerField(choices=((0,'男'),(1,'女'),),verbose_name='性别')
    telephone = models.CharField(max_length=11,verbose_name='手机号')
    id_num = models.CharField(max_length=18,verbose_name='身份证')

    class Meta:
        db_table = "patient"
        verbose_name = "就诊人"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s" % self.name

    @property
    def sex_cn(self):
        return self.get_sex_display()


class hospital(BaseModel):
    hospital_level = (
        (0,'三甲'),
        (1,'三级'),
        (2,'二级'),
        (3,'社区'),
    )
    name = models.CharField(max_length=32,verbose_name='名字')
    district = models.CharField(max_length=128,verbose_name='所属区')
    level = models.IntegerField(choices=hospital_level,verbose_name='医院级别')
    address = models.CharField(max_length=128,verbose_name='医院具体地址')



    class Meta:
        db_table = "hospital"
        verbose_name = "医院"
        verbose_name_plural = "医院"

    def __str__(self):
        return "%s" % self.name


class Order(models.Model):
    status_choices = (
        (0, '未支付'),
        (1, '已支付'),
        (2, '已取消'),
        (3, '超时取消'),
    )
    pay_choices = (
        (1, '支付宝'),
        (2, '微信支付'),
    )
    subject = models.CharField(max_length=150, verbose_name="订单标题")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="订单总价", default=0)
    out_trade_no = models.CharField(max_length=64, verbose_name="订单号", unique=True)
    trade_no = models.CharField(max_length=64, null=True, verbose_name="流水号")  # 支付宝生成回来的
    order_status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="订单状态")
    pay_type = models.SmallIntegerField(choices=pay_choices, default=1, verbose_name="支付方式")
    pay_time = models.DateTimeField(null=True, verbose_name="支付时间")
    # 一个用户可以下多个订单，一个订单只属于一个用户，一对多的关系，关联字段写在多个一方，写在order方
    user = models.ForeignKey(User, related_name='order_user', on_delete=models.DO_NOTHING, db_constraint=False, verbose_name="下单用户")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')


    class Meta:
        db_table = "accompany_order"
        verbose_name = "订单记录"
        verbose_name_plural = "订单记录"

    def __str__(self):
        return "%s - ￥%s" % (self.subject, self.total_amount)