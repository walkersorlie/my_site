from django.test import TestCase
from django.utils.text import slugify
from django.urls import reverse, resolve
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
# Test 5: Editing a blog post title does not change the slug
# Test 6: Blog homepage shows 3 latest blog posts
# Test 7: If only 1 blog post, blog homepage only shows that blog
# Test 8: Viewing a blog post shows the correct post based on slug
# Test 9: Can't create a blog post without being logged in
# Test 10: Can't update a blog post without being logged in
# Test 11: Can't remove a blog post without being logged in
# Test 12: Password hashes correctly
# Test 13: Create User corectly

def create_user(username, password, email_address):
    return User.objects.create(username=username, password=password, email_address=email_address)



class CreatePostWithLogin(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.user = User.objects.create(username='username', password='password', email_address='test@test.com')

    def test_create_post_not_logged_in(self):
        response = self.client.get(reverse('blog:create-post'))
        self.assertRedirects(response, '/login/', status_code=302, target_status_code=200)

    """
    def test_create_post_logged_in(self):
        # need to simulate login here, before request
        response = self.client.get(resolve('blog:create-post'))
        self.assertEquals(response.func.view_class, CreatePostView)
        # self.assertEquals(response.view_class, 'create-post')
    """

# class CreateUserTest(TestCase):
    # def test_create_user_successfully(self):
    #     old_total_users = User.objects.count()
    #     user = create_user('test-user', 'password', 'test@test.com')
    #     new_total_users = User.objects.count()
    #     self.assertGreater(new_total_users, old_total_users)

# class BlogCreatePostTests(TestCase):
    # def test_create_blog_post_successfully(self):
    #     old_total_posts = Post.objects.count()
    #     test_post = Post(author_id=create_user('test-userr2', 'Password', 'test2@test.com'), title='test title', body='test body', pub_date=datetime.now(), slug=slugify('test title'))
    #     new_total_posts = Post.objects.count()
    #     self.assertGreater(new_total_posts, old_total_posts)
