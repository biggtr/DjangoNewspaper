from django.urls import path
from .views import ArticleListView

urlpatterns = [path("", ArticleListView, name="article_list")]
