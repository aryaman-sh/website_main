from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . import models
from django.http import HttpResponse


def home(request):
    articles = models.Article.objects.all().order_by('date')
    return render(request, 'articles/index.html', {'articles': articles})


def add_article(request):
    if request.method == "GET":
        form = forms.CreateArticle()
    else:
        # method is post
        form = forms.CreateArticle(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:home')
    return render(request, 'articles/add_article.html', {'form': form})


def article_page(request, article_id):
    try:
        article = models.Article.objects.get(id=article_id)
    except models.Article.DoesNotExist:
        return redirect('articles:home')
    return render(request, 'articles/article_detail.html', {'article': article})


def update_article(request, article_id):
    if request.method == "GET":
        article = get_object_or_404(models.Article, id=article_id)
        form = forms.UpdateArticle(initial={'title': article.title, 'date': article.date, 'body': article.body})
    else:
        article = get_object_or_404(models.Article, id=article_id)
        form = forms.UpdateArticle(request.POST)
        if form.is_valid():
            form.save()
        article.delete()
        return redirect('articles:home')

    return render(request, 'articles/update.html', {'form': form, 'article': article})
