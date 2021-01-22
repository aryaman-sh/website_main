from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]
