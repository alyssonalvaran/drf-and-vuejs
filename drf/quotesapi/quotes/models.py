from django.db import models

from django.contrib.auth.models import User

class Quote(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    quote_author = models.CharField(max_length=60)
    quote_body = models.TextField()
    context = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=140, blank=True, null=True)

    def __str__(self):
        return self.quote_body
