from django.urls import include, re_path,path
from django.contrib import admin
from app_articles.views import apiclassViewAllArticles,apiclassArticleDetailView,ListArticlesMixins, apiclass_ArticleDeleteView
from app_articles import views



app_name='app_articles'

urlpatterns = [
    path('articles/',apiclassViewAllArticles.as_view(), name='dashboard_articles'),

    #-----

    path('articleListMixin/',ListArticlesMixins.as_view(), name='articleListMixin'),

    path('article_create',views.article_create, name='article_create'),
    path('article_delete/<int:pk>',apiclass_ArticleDeleteView.as_view(), name='article_delete'),

    path('articleDetailView/<int:pk>',apiclassArticleDetailView.as_view(), name='articleDetailView'),


    
]

