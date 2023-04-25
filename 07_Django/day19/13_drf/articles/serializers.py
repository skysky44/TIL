from rest_framework import serializers
from .models import Article,Comment
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


# 순서 위로 올림
class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__' # 모든 필드를 is_valid 하겠다.라는 의미
            # fields = ('content',)
            # 유효성 검사에서는 제외시키고, 데이터 조회시에는 제공(읽기 전용 속성)
            read_only_fields = ('article',)





class ArticleSerializer(serializers.ModelSerializer):
    
    # fields를 조절하고 싶으면 serializer를 새로 만들어도 됨
    # 여기서만 쓰는 serializer이면 class 안에 넣어도 됨
    class MyCommentSerializer(serializers.ModelSerializer):
            class Meta:
                model = Comment
                fields = ('id','content',) 
                read_only_fields = ('article',)

    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # 읽기전용
    # comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # 역참조 이름 변경(models.py에서 related name 지정후)

    # 위의 CommentSerializer를 추가(전체 댓글 조회를 위해서)
    comment_set = MyCommentSerializer(many=True, read_only=True)
    # id','content 두개만 보여주기위해 MyCommentSerializer 새로 만듦

    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True) # 특이함.. 역참조 결과를 센 결과

    class Meta:
        model = Article
        fields = '__all__'
        # read_only_fields = ('comment_set',) 안됨 all에 포함된 것이 아니기 때문에(article에 포함된 물리적 필드가 아니기 때문)

