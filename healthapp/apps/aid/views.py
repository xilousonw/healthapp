from django.shortcuts import render

# Create your views here.

from healthapp.utils.response import APIResponse
from healthapp.utils.logger import log

from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from django.conf import settings
from django.core.cache import cache
from rest_framework.response import Response
from . import models
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter



class AidView(GenericViewSet,ListModelMixin):
    queryset = models.Aid.objects.filter(is_delete=False, is_show=True)
    serializer_class = serializers.AidSerializer


class SymptomView(GenericViewSet,ListModelMixin):
    queryset = models.Symptom.objects.filter(is_delete=False, is_show=True)
    serializer_class = serializers.SymptonSerializer


from . import filters
class DrugView(GenericViewSet,ListModelMixin):
    queryset = models.Drug.objects.filter(is_delete=False, is_show=True)
    serializer_class = serializers.DrugListSerializer

    #通过对'drug_kind','drug_otc','drug_yibao'字段进行过滤来筛选药品
    # filter_backends = [DjangoFilterBackend, filters.DrugFilterSet]
    # filter_fields = ['drug_kind','drug_otc','drug_yibao']


class DrugDetailView(GenericViewSet,RetrieveModelMixin):
    queryset = models.Drugdetail.objects.filter(is_delete = False, is_show=True)
    serializer_class = serializers.DrugDetailSerializer


