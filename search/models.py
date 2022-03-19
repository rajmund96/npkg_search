from django.db import models


class Package(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    author_name = models.CharField(max_length=255, null=True, blank=True)
    author_email = models.EmailField(null=True, blank=True)
    version = models.CharField(max_length=255, null=True, blank=True)
    maintainer_email = models.EmailField(null=True, blank=True)
    maintainer_name = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField(max_length=128, blank=True, null=True)
