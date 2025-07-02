from django.db import models
from todo.models import Todo
from django.contrib.auth.models import User

# 좋아요 모델
class Like(models.Model):
    # 공통필드
    # 개별필드
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)

    class Meta:
        unique_together = ("user", "todo")
        # 중복 데이터를 방지해 주는 조건

    def __str__(self):
        return f"{self.user.username} ❤️ {self.todo.name}"
        # admin ❤️ 공부하기 

# 북마크 모델
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    is_bookmarked = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ("user", "todo")
        # 중복 데이터를 방지해 주는 조건

    def __str__(self):
        return f"{self.user.username} ❤️ {self.todo.name}"


# 댓글 모델
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # 각 댓글 별도의 좋아요 기능
    likes = models.ManyToManyField(User, through ="CommentLike", related_name="liked_comments", blank=True)

    def __str__(self):
        return f"{self.user.username} ❤️ {self.content[:20]}"


# 언제 누가 어떤 댓글에 좋아요를 남겼는지 기록
class CommentLike(models.Model):
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
    # 사용자가 댓글에 좋아요를 누른 시간을 자동으로 저장하기 위한 필드
    
    is_like = models.BooleanField(default=True)
    # 현재 좋아요가 유효한지 여부를 나타내는 bool 값


    class Meta:
        unique_together = ("comment", "user")

    def __str__(self):
        return f"{self.user.username} ❤️ {self.comment.id}"

# 모델의 역할
#비즈니스 로직을 처리한다.
#데이터 저장, 검증 처리
#어떤 값이 나와야 하는지 처리