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


class DrugDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Drug
        fields = "__all__"
