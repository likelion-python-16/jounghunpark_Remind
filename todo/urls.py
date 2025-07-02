from django.urls import path ,include
from . import views
from . import api_views
from .api_views import * 
from rest_framework.routers import DefaultRouter

app_name = "todo"

router = DefaultRouter()
router.register("view", TodoViewSet, basename="todo")



urlpatterns = [
    # path("list/", views.todo_list, name="todo_List"), # list 목록보기 

    # 탬플릿Views
    path("list/", views.TodoListViews.as_view(), name="todo_List"), # list 목록보기
    path("create/", views.TodoCreateViews.as_view() , name="todo_Create"),
    path("detail/<int:pk>/", views.TodoDetailViews.as_view(), name="todo_Detail"),
    path("update/<int:pk>/", views.TodoUpdateViews.as_view(), name="todo_Update"),

    # # apiViews
    # path("api/list/", TodoGenericsListAPI.as_view(), name="todo_api_list"),
    # path("api/create/", api_views.TodoCreateAPI.as_view(), name="todo_api_create"),
    # path("api/retrieve/<int:pk>/", api_views.TodoRetrieveAPI.as_view(), name="todo_api_retrieve"),
    # path("api/update/<int:pk>/",api_views.TodoUpdateAPI.as_view(), name="todo_api_update"),
    # path("api/delete/<int:pk>/",api_views.TodoDeleteAPI.as_view(), name="todo_api_delete"),

    # #GenericAPIView
    # path("Generic/list/", api_views.TodoListAPI.as_view(), name="todo_api_list"),
    # path("Generic/create/", TodoGenericsCreateAPI.as_view(), name="todo_api_create"),
    # path("Generic/retrieve/<int:pk>/", TodoGenericsRetrieveAPI.as_view(), name="todo_api_retrieve"),
    # path("Generic/update/<int:pk>/",TodoGenericsUpdateAPI.as_view(), name="todo_api_update"),
    # path("Generic/delete/<int:pk>/",TodoGenericsDeleteAPI.as_view(), name="todo_api_delete"),

    # #GenericAPIView + Mixin
    # path("Generics/", TodoGenericsListCreateAPI.as_view(), name="todo_generics_list_create"),
    # path("Generics/<int:pk>/", TodoGenericsRetrieveUpdateDeleteAPI.as_view(), name="todo_generics_detail"),

    #viewSets
    path("viewsets/", include(router.urls)), # /todo/viewsets/view/


    # logaut API

    path("api/custom-logout/", CustomLogoutAPI.as_view(), name="custom-logout"),



]