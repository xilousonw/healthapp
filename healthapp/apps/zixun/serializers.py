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


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.comment
        fields = ['username', 'content', 'cmt_time', 'cmt_thumbup']
        extra_kwargs = {
            'id': {'read_only': True}
        }


    def _filter_bad_words(self,attrs):
        content = attrs.get('content')
        badword_list = ['sb','傻逼','弱智']
        for badword in badword_list:
            if badword in content:
                content.replace('**', badword)
                raise ValidationError('包含敏感词')
        return content

    # def create(self, validated_data):
    #     comment = models.comment.save(**validated_data)
    #     return comment