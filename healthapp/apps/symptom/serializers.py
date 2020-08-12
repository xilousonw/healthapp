from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError

from django.conf import settings


class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.body
        fields = ['id','name',]
        extra_kwargs = {
            'id': {'read_only': True},
        }


class OrganSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.organ
        fields = ['id','name']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.symptom
        fields = ['id','name']
        extra_kwargs = {
            'id': {'read_only': True},
        }