from django.db import models


class Repository(models.Model):
    repo_name = models.CharField('Repository', max_length=300)    # Make unique??? Test later
    description = models.TextField()
    pushed_at = models.DateTimeField()
    url = models.URLField(max_length=400)
    github_repo_id = models.CharField(max_length=300, unique=True)


    class Meta:
        ordering = ['-pushed_at']
        verbose_name_plural = "Repositories"

    def __str__(self):
        return self.repo_name.replace('-', ' ').replace('_', ' ').title()
        # return self.repo_name

    def save(self, *args, **kwargs):
        self.repo_name = self.repo_name.replace(' ', '-')
        super().save(*args, **kwargs)
