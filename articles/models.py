from django.db import models
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    body = models.TextField(verbose_name='Message')
    slug = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(null=True, blank=True)

    is_public = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.title, self.created_at)


    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)
