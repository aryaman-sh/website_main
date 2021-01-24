from django import forms
from . import models


class CreateTodo(forms.ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ['item', 'created', 'due']


class UpdateTodo(forms.ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ['item', 'due']