from .models import Like, Bookmark, Comment , CommentLike
from rest_framework import serializers


# user.username, todo.name

class LikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    # 외래키를 통해 확인용으로 저장
    todo_name = serializers.CharField(source="todo.name", read_only=True)

    class Meta:
        model = Like
        fields = ["id", "todo", "todo_name", "user", "username", "is_like"]
        read_only_fields =["user"]
        

class BookmarkSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    todo_name = serializers.CharField(source="todo.name", read_only=True)

    class Meta:
        model = Bookmark
        fields = ["id", "todo", "todo_name", "user", "username", "is_marked"]
        read_only_fields =["user"]

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    todo_name = serializers.CharField(source="todo.name", read_only=True)
    like_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "todo", "todo_name", "user", "username", "content", "created_at","like_count,","is_liked"]
        read_only_fields =["todo","user","created_at"]

        def get_like_count(self, obj):
            return obj.likes.count()
        

        def get_is_liked(self, obj):
            request = self.context.get("request")
            if request and request.user.is_authenticated:
                return obj.likes.filter(id=request.user.id).exists()
            return False


# 시리얼라이저의 역할
# 유효성 검증, 프레젠테이션 로직을 처리한다.
# 화면에 표시되는 박식, 스타일관련 로직 처리

# M2M 추가
class CommentLikeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    
    comment_content = serializers.CharField(source="comment.content", read_only=True)

    class Meta:
        model = CommentLike
        fields = ["id", "user", "username", "comment", "comment_content", "is_like", "liked_at"]
        read_only_fields =["user", "liked_at"]

from rest_framework.serializers import ModelSerializer
from .models import Todo
from rest_framework import serializers

class TodoSerializer(ModelSerializer):
    # ✅ 선언 필수!!
    like_count = serializers.SerializerMethodField() #
    is_liked = serializers.SerializerMethodField() #
    is_bookmarked   = serializers.SerializerMethodField() #     
    bookmark_count = serializers.SerializerMethodField() #
    comment_count = serializers.SerializerMethodField() 

    class Meta:
        model = Todo
        fields = [  # ✅ 여기 명시적으로 선언!
            'id', 'name', 'description', 'complete', 'completed_at',
            'exp', 'image', 'created_at', 'updated_at',
            'like_count', 'is_liked', 'is_bookmarked', 'bookmark_count', 'comment_count', 
        ]
        read_only_fields = ['completed_at'] # ✅ 필드가 없어도 찾기 않고 읽고 넘기도록 처리

    # ✅ 오버라이딩 처리 필드 선언한 것에 대한 세부함수
    def get_like_count(self, obj):
        return obj.like_set.filter(is_like=True).count()  # 연결된 Like 모델 기준

    def get_is_liked(self, obj):
        user = self.context['request'].user
        return bool(user.is_authenticated and obj.like_set.filter(user=user, is_like=True).exists())

    def get_is_bookmarked(self, obj):
        user = self.context['request'].user
        return bool(user.is_authenticated and
                obj.bookmark_set.filter(user=user, is_marked=True).exists())
    
    def get_bookmark_count(self, obj):
        return obj.bookmark_set.filter(is_marked=True).count()

    def get_comment_count(self, obj):                   
        return obj.comment_set.count()