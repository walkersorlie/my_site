from django.db import models

class Repository(models.Model):
    repo_name = models.CharField(max_length=300)
    description = models.TextField()
    pushed_at = models.DateTimeField()
    url = models.URLField(max_length=400)
