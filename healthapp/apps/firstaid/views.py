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



class FirstaidView(GenericViewSet,ListModelMixin):
    queryset = models.Firstaid.objects.filter(is_delete=False, is_show=True)
    serializer_class = serializers.FirstaidSerializer

    # def list(self,request, *args, **kwargs):
    #     firstaid_list = cache.get('firstaid_list')
    #     if not firstaid_list:
    #         response = super().list(request, *args, **kwargs)
    #         cache.set('firstaid_list',response.data,60*60*24)
    #         return response
    #     return Response(data=firstaid_list)



#
class FirstaidDetailView(GenericViewSet,RetrieveModelMixin):
    queryset = models.Firstaid.objects.filter(is_delete=False, is_show=True)
    serializer_class = serializers.FirstaidDetailSerializer

