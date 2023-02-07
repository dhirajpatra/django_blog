from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# Post to be indexed into ElasticSearch
class Post(models.Model):
    title = models.CharField(
        _('title'),
        max_length=200
    )
    pub_date = models.DateTimeField(
        _('pub_date'),
        auto_now_add=True
    )
    body = models.TextField(
        _('body'),
        max_length=1000
    )

    def __str__(self):
        return self.title

    # def get_action_title(self):
    #     return '{} - {}'.format(self.title, self.pub_date)

    class Meta:
        app_label = 'blog'
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        get_latest_by = "pub_date"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.TextField(max_length=100)

    def __str__(self):
        return self.title

