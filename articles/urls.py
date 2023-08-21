from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
)

urlpatterns = [
    path("", ArticleListView, name="article_list"),
    path("<int:pk>/", ArticleDetailView, name="article_detail"),
    path("create/", ArticleCreateView, name="article_create"),
    path("<int:pk>/update/", ArticleUpdateView, name="article_update"),
    path("<int:pk>/delete/", ArticleDeleteView, name="article_delete"),
]
