from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError

from django.conf import settings


class AccompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.accompany
        fields = ['id','accompany','accompany_name', 'serve_time_gap', 'serve_process', 'serve_content']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.appointment
        fields = ['id','hospital', 'patient', 'ap_time', 'price']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.patient
        fields = ['id','name','sex','telephone','id_num']
        extra_kwargs={
            'id':{'read_only':True},
        }


class PatientAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.patient
        fields = ['id','name','sex','telephone','id_num']
        extra_kwargs={
            'id':{'read_only':True},
        }


class HostpitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.hospital
        fields = ['id','name', 'district', 'level','level_name', 'address']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class OrderSerializer(serializers.ModelSerializer):
    # 前端传什么数据过来{course:[1,2,3],total_amount:100,subject:xx商品,pay_type:1,}
    # user字段需要，但是不是传的，使用了jwt
    class Meta:
        model = models.Order
        fields = ['total_amount','pay_type','appointment']
        extra_kwargs={
            'total_amount':{'required':True},
            'pay_type': {'required': True},
        }


    def _check_price(self,attrs):
        total_amount=attrs.get('total_amount')
        course_list=attrs.get('course')
        total_price=0
        for course in course_list:
            total_price+=course.price
        if total_price!=total_amount:
            raise ValidationError('价格不合法')
        return total_amount


    def _gen_out_trade_no(self):
        import uuid
        return str(uuid.uuid4()).replace('-','')


    def _get_user(self):
        # 需要request对象(需要视图通过context把reuqest对象传入。重写create方法)
        request=self.context.get('request')
        return request.user

    def _gen_pay_url(self,out_trade_no,total_amout,subject):
        # total_amout是Decimal类型，识别不了，需要转换成float类型
        from healthapp.libs.al_pay import alipay,gateway
        order_string = alipay.api_alipay_trade_page_pay    (
            out_trade_no=out_trade_no,
            total_amount=float(total_amout),
            subject=subject,
            return_url=settings.RETURN_URL,  # get回调，前台地址
            notify_url=settings.NOTIFY_URL   # post回调，后台地址
        )
        return gateway+order_string

    def _before_create(self,attrs,user,pay_url,out_trade_no):
        attrs['user']=user
        attrs['out_trade_no']=out_trade_no

        self.context['pay_url']=pay_url
    def validate(self, attrs):
        '''
        # 1）订单总价校验
        # 2）生成订单号
        # 3）支付用户：request.user
        # 4）支付链接生成
        # 5）入库(两个表)的信息准备
        '''
        # 1）订单总价校验
        total_amout = self._check_price(attrs)
        # 2）生成订单号
        out_trade_no=self._gen_out_trade_no()
        # 3）支付用户：request.user
        user=self._get_user()
        # 4）支付链接生成
        pay_url=self._gen_pay_url(out_trade_no,total_amout,attrs.get('subject'))
        # 5）入库(两个表)的信息准备
        self._before_create(attrs,user,pay_url,out_trade_no)

        return attrs



    def create(self, validated_data):
        course_list=validated_data.pop('course')
        order=models.Order.objects.create(**validated_data)
        for course in course_list:
            models.OrderDetail.objects.create(order=order,course=course,price=course.price,real_price=course.price)

        return order