from django.shortcuts import render

# Create your views here.

from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from django.conf import settings
from django.core.cache import cache
from rest_framework.response import Response
from . import models
from . import serializers
from healthapp.utils.response import APIResponse
# from healthapp.apps.user.models import User


class NewsView(GenericViewSet,ListModelMixin):
    queryset = models.news.objects.filter(is_delete=False, is_show=True)
    serializer_class = serializers.NewsSerializer


class NewsDetailView(GenericViewSet,RetrieveModelMixin):
    queryset = models.news_detail.objects.filter(is_delete=False,is_show=True)
    serializer_class = serializers.NewsDetailSerializer


class CommentView(GenericViewSet,CreateModelMixin):
    # queryset = models.comment.objects.filter(is_delete=False,is_show=True)
    queryset =  models.comment.objects.all()
    serializer_class = serializers.CommentSerializer

    # def post(self,request):
    #     return self.create(request)

    # def create(self, request, *args, **kwargs):
    #     response=super().create(request, *args, **kwargs)
    #     return APIResponse(code=1,msg='评论成功')



# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# class CommentsView(GenericViewSet,CreateModelMixin):
#     authentication_classes = [JSONWebTokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = models.comment.objects.filter(is_delete=False,is_show=True)
#
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)


