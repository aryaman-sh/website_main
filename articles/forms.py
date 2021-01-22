from django import forms
from . import models


class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'date', 'body']


class UpdateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'date', 'body']