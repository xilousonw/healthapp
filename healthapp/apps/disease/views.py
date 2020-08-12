from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,ListModelMixin,DestroyModelMixin,RetrieveModelMixin
from . import models
from . import serializers
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView



class DiseaseView(GenericViewSet,ListModelMixin):
    queryset = models.disease.objects.filter(is_delete=False,is_show=True)
    serializer_class = serializers.DiseaseSerializer


class DiseaseDetailView(GenericViewSet,RetrieveModelMixin):
    queryset = models.disease.objects.filter(is_delete=False,is_show=True)
    serializers_class = serializers.DiseaseDetailSerializer

