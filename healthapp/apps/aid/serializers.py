from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError

class AidSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Aid
        fields = ['id','name']


class SymptonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Symptom
        fileds = ['id', 'name']


class DrugListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Drug
        fields = ['name','drug_kind','drug_otc','drug_yibao']


class DrugDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Drugdetail
        fields = "__all__"
