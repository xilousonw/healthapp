from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError

# from django.conf import settings

class FirstaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Firstaid
        fields = ['c_name']
        # extra_kwargs = {
        #     'id':{'read_only':True}
        # }


class FirstaidDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Firstaid
        fields = ['id','c_name','e_name','makecall','do_steps','go_doctor']
        # extra_kwargs = {
        #     'id':{'read_only':True}
        # }
