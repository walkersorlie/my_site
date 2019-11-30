from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe


class Repository(models.Model):
    repo_name = models.CharField('Repository', max_length=300)    # Make unique??? Test later
    description = models.TextField()
    pushed_at = models.DateTimeField()
    url = models.URLField(max_length=400)
    github_repo_id = models.CharField(max_length=300, unique=True)


    class Meta:
        ordering = ['-pushed_at']


    def __str__(self):
        return self.repo_name.replace('-', ' ').replace('_', ' ').title()
        # return self.repo_name

    def save(self, *args, **kwargs):
        self.repo_name = self.repo_name.replace(' ', '-')
        super().save(*args, **kwargs)


class AboutContent(models.Model):
    body = models.TextField()
    last_edited = models.DateTimeField()

    def __str__(self):
        return "About block content"

    def save(self, *args, **kwargs):
        self.body = self.display_my_safefield()
        self.last_edited = timezone.now()
        super(AboutContent, self).save(*args, **kwargs)

    """
    Has to do with encoding it looks like???
    HTML symbols
    https://bleach.readthedocs.io/en/latest/clean.html
    """
    def display_my_safefield(self):
        if '<script>' in self.body:
            return self.body
        return mark_safe(self.body)
