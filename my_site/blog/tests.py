from django.test import TestCase
from django.utils.text import slugify
from datetime import datetime
from blog.models import User, Post

"""
Run with options:
 --keepdb, -k
"""
# Test 1: Create a blog post successfully
# Test 2: Update a blog post successfully
# Test 3: Remove a blog post successfully
# Test 4: Can't create a blog posts with the same title
# Test 5: Editing a blog post title does not change the slugs
# Test 6: Blog homepage shows 3 latest blog posts
# Test 7: If only 1 blog post, blog homepage only shows that blog
# Test 8: Viewing a blog post shows the correct post based on slug
# Test 9: Can't create a blog post without being logged in
# Test 10: Can't update a blog post without being logged in
# Test 11: Can't remove a blog post without being logged in
# Test 12: Password hashes correctly
# Test 13: Create User corectly

GLOBAL_USER = User(username='test-user', password='password', email_address='test@test.com')
GLOBAL_USER.save()

class CreateUserTest(TestCase):
    def test_create_user_successfully(self):
        GLOBAL_USER = User(username='test-user', password='password', email_address='test@test.com')
        old_total_users = User.objects.count()
        GLOBAL_USER.save()
        new_total_users = User.objects.count()
        self.assertGreater(new_total_users, old_total_users)

class BlogCreatePostTests(TestCase):
    def test_create_blog_post_successfully(self):
        test_post = Post(author_id=GLOBAL_USER, title='test title', body='test body', pub_date=datetime.now(), slug=slugify('test title'))
        old_total_posts = Post.objects.count()
        test_post.save()
        new_total_posts = Post.objects.count()
        self.assertGreater(new_total_posts, old_total_posts)
