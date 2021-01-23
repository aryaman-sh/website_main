from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


class Article(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    body = models.TextField()
    author = models.ForeignKey(User, default=None, on_delete=CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100] + "..."
