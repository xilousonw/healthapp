from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError

from django.conf import settings

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.news
        fields = ['id','title', 'news_img', 'checked', 'catagory_name','catagorys','recommended']
        extra_kwargs = {
            'id':{'read_only':True}
        }


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.news_detail
        fields = ['id','title','author','article', 'date', 'news_detail_img','thumbup']
        extra_kwargs = {
            'id':{'read_only':True}
        }
