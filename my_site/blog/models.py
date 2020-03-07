from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User as Auth_User
from django.utils import timezone


class Post(models.Model):
    """
    'author_id' is not the primary key ID of the user, it's the username
    """
    # author_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='author_id')
    author_id = models.ForeignKey(Auth_User, on_delete=models.CASCADE, db_column='author_id')
    title = models.CharField(max_length=300)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    slug = models.SlugField(max_length=100, unique=True, blank=True) # don't query on slug. slow


    class Meta:
        ordering = ['-pub_date']


    def get_absolute_url(self):
        return reverse('blog:view_post', args=[self.slug])

    def __str__(self):
        return "title: " + f'"{self.title}"' + ", author: " + self.author_id.username.capitalize()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            self.pub_date = timezone.now()

        super(Post, self).save(*args, **kwargs)
