from django.urls import path

from . import views
app_name = 'thread'

urlpatterns = [
    path('create_topic/', views.TopicCreateViewBySession.as_view(), name='create_topic'),
    path('<int:pk>/', views.TopicAndCommentView.as_view(), name='topic'),
    path('category/<str:url_code>/', views.CategoryView.as_view(), name='category'), #クラスビュー
    #path('category//', views.show_category, name='category'), #関数ビュー
]