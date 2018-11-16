from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "title: " + f'"{self.title}"' + ", author username: " + self.author_id.username
