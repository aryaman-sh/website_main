from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'articles'

urlpatterns = [
    path('', views.home, name="home"),
    path('add_article/', views.add_article, name="add_article"),
    path('article_page/<int:article_id>/', views.article_page, name="details"),
    path('update_article/<int:article_id>/', views.update_article, name="update")
]
