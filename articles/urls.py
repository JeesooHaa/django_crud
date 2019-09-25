from django.urls import path 
from . import views 

app_name = 'articles'
# /articles/__ 
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),  # url 에 이름 짓기 
    path('<int:article_pk>/delete/', views.delete, name='delete'),  
    path('create/', views.create, name='create'),  # mapping
    path('<int:article_pk>/edit/', views.edit, name='edit'),
    path('selected/', views.selected, name='selected'), 
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    # /article/3/commnets/2/delete
    path('<int:comment_pk>/comments_delete/', views.comments_delete, name='comments_delete'),
]
