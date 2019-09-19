from django.urls import path 
from . import views 

# /articles/__ 
urlpatterns = [
    path('', views.index),
    path('<int:article_pk>/', views.detail),   
    path('delete/<int:article_pk>/', views.delete),  
    path('new/', views.new),
    path('create/', views.create),  # mapping
]
