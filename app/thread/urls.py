from django.urls import path

from . import views
app_name = 'thread'


urlpatterns = [
    # path('create_topic/', views.TopicCreateViewBySession.as_view(), name='create_topic'),
    path('create_topic/', views.TopicCreateView.as_view(), name='create_topic'),
    # path('create_topic/', views.topic_create, name='create_topic'),
    path('<int:pk>/', views.TopicAndCommentView.as_view(), name='topic'),
    # path('category//', views.CategoryView.as_view(), name='category'),
    path('category/<str:url_code>/', views.show_category, name='category'),
]