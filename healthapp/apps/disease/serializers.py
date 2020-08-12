from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError

# from django.conf import settings

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.disease
        fields = ['id','c_name']
        # extra_kwargs = {
        #     'id':{'read_only':True}
        # }


class DiseaseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.disease
        fields = ['id','c_name','e_name','makecall','do_steps','go_doctor']
        # extra_kwargs = {
        #     'id':{'read_only':True}
        # }
