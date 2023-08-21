from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article

# Create your views here.


def ArticleListView(request):
    articles = Article.objects.all()
    return render(request, "article_list.html", context={"article_list": articles})


def ArticleDetailView(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "article_detail.html", context={"object": article})


@login_required
def ArticleCreateView(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("article_list")

    else:
        form = ArticleForm()
    return render(request, "article_create.html", context={"form": form})


@login_required
def ArticleUpdateView(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("article_list")
    else:
        form = ArticleForm(instance=article)
    return render(request, "article_update.html", context={"form": form})


@login_required
def ArticleDeleteView(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect("article_list")
    return render(request, "article_delete.html", context={"article": article})
