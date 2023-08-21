from django.shortcuts import render, redirect
from .models import Article

# Create your views here.


def ArticleListView(request):
    articles = Article.objects.all()
    return render(request, "article_list.html", context={"article_list": articles})
