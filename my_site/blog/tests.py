from django.test import TestCase
from datetime import datetime
import blog.models

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

user = None

class CreateUserTest(TestCase):
    def create_user_successfully(self):
        user = User(username='test-user', password='password', email_address='test@test.com')
        total_users = User.objects.count()
        user.save()
        self.assert

class BlogCreatePostTests(TestCase):
    def create_blog_post_successfully(self):
        test_post = Post(author_id=user, title='test title', body='test body', pub_date=datetime.now(), slug=slugify('test title'))
