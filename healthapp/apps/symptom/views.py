from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,ListModelMixin,DestroyModelMixin
from . import models
from . import serializers
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView



class BodyView(GenericViewSet,ListModelMixin):
    queryset = models.body.objects.filter(is_delete=False,is_show=True)
    serializer_class = serializers.BodySerializer


class OrgamView(GenericViewSet,ListModelMixin):
    queryset = models.organ.objects.filter(is_delete=False,is_show=True)
    serializer_class = serializers.OrganSerializer


class SymptomView(GenericViewSet,ListModelMixin):
    queryset = models.symptom.objects.filter(is_delete=False,is_show=True)
    serializer_class = serializers.SymptomSerializer


class MySymptomView(GenericViewSet,CreateModelMixin,DestroyModelMixin):
    queryset = models.symptom.objects.filter(is_delete=False,is_show=True)
    serializers_class = serializers.SymptomSerializer


class SymptomResultView(GenericViewSet,CreateModelMixin,ListModelMixin):
    queryset = models.symptom.objects.filter(is_delete=False, is_show=True)
    serializers_class = serializers.SymptomSerializer
