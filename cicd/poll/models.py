from django.db import models

# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

