from django.db import models


class Repository(models.Model):
    repo_name = models.CharField(max_length=300)    # Make unique??? Test later
    description = models.TextField()
    pushed_at = models.DateTimeField()
    url = models.URLField(max_length=400)
    github_repo_id = models.CharField(max_length=300)

    def __str__(self):
        return self.repo_name
