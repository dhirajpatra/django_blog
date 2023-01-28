from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
