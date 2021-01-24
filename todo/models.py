from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


class TodoItem(models.Model):
    item = models.CharField(max_length=300)
    author = models.ForeignKey(User, default=None, on_delete=CASCADE)
    due = models.DateTimeField(null=True)
    created = models.DateTimeField()
