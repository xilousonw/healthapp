from django.shortcuts import render

# Create your views here.

from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from django.conf import settings
from django.core.cache import cache
from rest_framework.response import Response
from . import models
from . import serializers

class NewsView(GenericViewSet,ListModelMixin):
    queryset = models.news.objects.filter(is_delete=False, is_show=True)
    serializer_class = serializers.NewsSerializer


class NewsDetailView(GenericViewSet,RetrieveModelMixin):
    queryset = models.news_detail.objects.filter(is_delete=False,is_show=True)
    serializer_class = serializers.NewsDetailSerializer
