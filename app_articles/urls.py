from django.urls import include, re_path,path
from django.contrib import admin
from app_articles.views import apiclass_ArticleView,article_detail_view

app_name='app_articles'
urlpatterns = [
    path('articles/',apiclass_ArticleView.as_view(), name='dashboard_articles'),

    path('articles/detail/<int:pk>',article_detail_view.as_view(), name='articleDetailView'),


]
