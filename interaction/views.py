from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from todo.models import Todo
from interaction.models import Like, Bookmark, Comment

# 로그인하지 않은 사용자가 이 뷰를 실행하지 못하도록 막아주는 데코레이션
@login_required # 로그인된 사용자만 접근 가능
def todo_detail_with_interaction(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    user = request.user

    like_obj = Like.objects.filter(todo=todo, user_id=user).first()
    like_count = Like.objects.filter(todo=todo, is_like=True).count()
    bookmark_obj = Bookmark.objects.filter(todo=todo, user=user).first()
    comments = Comment.objects.filter(todo=todo).order_by("created_at")
    is_liked = like_obj.is_like if like_obj else False
    
    context = {
        "todo": todo,
        "like_obj": like_obj,
        "is_liked" : is_liked,
        "like_count": like_count,
        "bookmark_obj": bookmark_obj,
        "comments": comments,

    }
    return render(request, "interaction/todo/detail.html", context)