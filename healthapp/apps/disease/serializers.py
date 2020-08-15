from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError

# from django.conf import settings

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.disease
        fields = ['id','name']
        # extra_kwargs = {
        #     'id':{'read_only':True}
        # }


class DiseaseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.disease
        fields = '__all__'
        # extra_kwargs = {
        #     'id':{'read_only':True}
        # }
