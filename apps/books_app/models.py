from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    title_name = models.CharField(max_length=38)
    author_name = models.CharField(max_length= 38)
    published_name = models.CharField(max_length=38)
    category_name = models.CharField(max_length= 38)
    in_print = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)