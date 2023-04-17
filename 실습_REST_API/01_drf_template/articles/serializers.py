from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        # GET할 때만 사용할 때
        read_only_fields = ('article',)
        # ~(read_only = True)

        # GET, POST, 등등 어디에도 쓰지 않는다
        # exclude = ['article'] 
            # validate_data 판별할 때 걸리짐(is_valid())
        # fields에 명시 X

    # 변수 이름만 바꿀거면 model.py에서 related_name을 쓰면 된다.
    # to_representation은 좀 더 복잡한 상황에서 사용
    # fields에 있는 변수 중 한두개를 뽑아 변형을 가하고 싶을 때
    # 보여줄 때
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = rep.pop('comment_set', [])
        return rep

    # 넣을 때
    # def to_internal_value(self, data):

class ArticleListSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)
        # fields = '__all__'

class ArticleDetailSerializer(serializers.ModelSerializer):
    # Nested Serializer
    comment_set = CommentSerializer(many=True)
    # 1. class Meta(ArticleListSerializer.Meta):
    class Meta:
        model = Article
        # 2. model = ArticleListSerializer.Meta.model
        fields = ArticleListSerializer.Meta.fields + ('comment_set')
