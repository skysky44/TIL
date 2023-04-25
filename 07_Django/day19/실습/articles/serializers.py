from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)



class ArticleSerializer(serializers.ModelSerializer):
    

    class MyCommentSerializer(serializers.ModelSerializer):
            class Meta:
                model = Comment
                fields = ('id','content',) 
                read_only_fields = ('article',)


    comment_set = MyCommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField (source='comment_set.count', read_only=True) 

    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__' 
            read_only_fields = ('article',)