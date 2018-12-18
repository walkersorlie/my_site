from django.db import models
from django.template.defaultfilters import slugify


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    """
    'author_id' is not the primary key ID of the user, it's the username
    """
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='author_id')
    title = models.CharField(max_length=300)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    slug = models.SlugField(max_length=100, unique=True, blank=True) # don't query on slug. slow

    def __str__(self):
        return "title: " + f'"{self.title}"' + ", author username: " + self.author_id.username


    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)
