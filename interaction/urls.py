from django.urls import path ,include
from rest_framework.routers import DefaultRouter 
from .api_views import LikeViewSet ,BookmarksViewSet, CommentsViewSet, CommentLikeViewSet
from .views import todo_detail_with_interaction


router = DefaultRouter()
router.register(r"likes", LikeViewSet, basename="likes")
router.register(r"bookmarks", BookmarksViewSet, basename="bookmarks")
router.register(r"comments", CommentsViewSet, basename="comments")  
router.register(r"commentlikes", CommentLikeViewSet, basename="commentlike")  
# r은 주소의 마지막을 표시한 것이며 규칙이 아닌 관습이다.

app_name = "interaction"

urlpatterns = [ 
    path("", include(router.urls)),
    path("todo/detail/<int:pk>/", todo_detail_with_interaction, name='todo_detail'),
]