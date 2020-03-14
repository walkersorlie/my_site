from django.test import TestCase, override_settings
from django.utils.text import slugify
from django.urls import reverse, resolve
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User as Auth_User
from django.contrib.auth import get_user_model
from . import models
from . import forms


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

# What happens if slug isn't unique??? (Not unique title)

def create_test_user(username, password):
    return Auth_User.objects.create_user(username=username, password=password)

def create_post(user, title, body):
    return models.Post.objects.create(author_id=user, title=title, body=body, pub_date=timezone.now(), slug=slugify(title))


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class BlogIndexViewPostsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        # cls.user = Auth_User.objects.create(username='username', password='password', email_address='test@test.com')
        # cls.user = create_test_user('test_user', 'password')
        cls.user = get_user_model().objects.create_user(username='test_user', password='password')
        # cls.second_user = get_user_model().objects.create_user(username='second_user', password='password2')
        # cls.post = models.Post.objects.create(author_id=cls.user, title='title', body='body', pub_date=timezone.now(), slug=slugify('title'))
        # cls.post = create_post(cls.user, 'Test Title', 'Test body')
    # def setUp(self):
    #     # Every test needs access to the request factory.
    #     self.factory = RequestFactory()
    #     self.user = create_user('test_user', 'password')


    def test_index_no_posts(self):
        response = self.client.get(reverse('blog:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts available at this time.")
        self.assertQuerysetEqual(response.context['post_list'], [])


    def test_index_view_posts(self):
        # post1 = models.Post.objects.create(author_id=self.user, title='Test Title', body='Test body', pub_date=timezone.now(), slug=slugify('Test Title'))
        # post2 = models.Post.objects.create(author_id=self.user, title='Test Title 2', body='Test body 2', pub_date=timezone.now(), slug=slugify('Test Title 2'))

        for x in range(1, 3):
            models.Post.objects.create(author_id=self.user, title=f'Test Title {x}', body=f'Test body {x}', pub_date=timezone.now(), slug=slugify(f'Test Title {x}'))

        response = self.client.get(reverse('blog:index'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['post_list'],
            ['<Post: title: "Test Title 2", author: Test_user>', '<Post: title: "Test Title 1", author: Test_user>'])


    def test_context_index_three_recent_posts_less_than_three(self):
        # create_post(self.user, 'Test Title', 'Test body')
        # create_post(self.user, 'Test Title 2', 'Test body 2')

        for x in range(1, 3):
            models.Post.objects.create(author_id=self.user, title=f'Test Title {x}', body=f'Test body {x}', pub_date=timezone.now(), slug=slugify(f'Test Title {x}'))

        response = self.client.get(reverse('blog:index'))

        self.assertEqual(response.status_code, 200)
        self.assertLessEqual(len(response.context['three_recent_posts']), 3)


    def test_context_index_three_recent_posts_more_than_three(self):
        """
        Now test that there are only 3 posts if the total number of posts is more than 3
        """
        # create_post(self.user, 'Test Title 3', 'Test body 3')
        # create_post(self.user, 'Test Title 4', 'Test body 4')
        for x in range(1, 5):
            models.Post.objects.create(author_id=self.user, title=f'Test Title {x}', body=f'Test body {x}', pub_date=timezone.now(), slug=slugify(f'Test Title {x}'))

        response = self.client.get(reverse('blog:index'))

        self.assertEqual(response.status_code, 200)
        self.assertLessEqual(len(response.context['three_recent_posts']), 3)


    def test_context_paginated_posts_empty(self):
        # create_post(self.user, 'Test Title', 'Test body')
        # create_post(self.user, 'Test Title 2', 'Test body 2')
        # create_post(self.user, 'Test Title 3', 'Test body 3')
        for x in range(1, 4):
            models.Post.objects.create(author_id=self.user, title=f'Test Title {x}', body=f'Test body {x}', pub_date=timezone.now(), slug=slugify(f'Test Title {x}'))

        response = self.client.get(reverse('blog:index'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['paginated_posts'], [])


    def test_context_paginated_posts_not_empty(self):
        """
        Now test 'paginated_posts' gets filled when there are more than 3 posts
        """
        # create_post(self.user, 'Test Title 4', 'Test body 4')
        for x in range(1, 5):
            models.Post.objects.create(author_id=self.user, title=f'Test Title {x}', body=f'Test body {x}', pub_date=timezone.now(), slug=slugify(f'Test Title {x}'))

        response = self.client.get(reverse('blog:index'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['paginated_posts']), 1)


    def test_view_post_view(self):
        # post = create_post(self.user, 'Test Title', 'Test body')
        post = models.Post.objects.create(author_id=self.user, title='Test Title', body='Test body', pub_date=timezone.now(), slug=slugify('Test Title'))

        response = self.client.get(reverse('blog:view_post', args=[post.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.body)



@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class BlogUserCreatePostsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='test_user', password='password')


    def test_create_post_redirect_if_not_authenticated(self):
        # response = self.client.get(reverse('blog:create_post'), follow=True)

        response = self.client.get(reverse('blog:create_post'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/registration/login/?next=/blog/create_post/')


    def test_create_post_logged_in_uses_correct_template(self):
        login = self.client.login(username='test_user', password='password')
        response = self.client.get(reverse('blog:create_post'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), self.user.get_username())
        self.assertTemplateUsed(response, 'blog/create_post.html')


    def test_blank_create_post_form(self):
        form = forms.PostForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'title': ['This field is required.'],
            'body': ['This field is required.'],
        })


    def test_valid_create_post_form(self):
        form_data = {
            'title': 'Test Title',
            'body': 'Test Body',
        }

        form = forms.PostForm(form_data)
        self.assertTrue(form.is_valid())

        created_post = form.save(commit=False)
        created_post.author_id = self.user
        created_post.pub_date = timezone.now(),
        created_post.save()

        self.assertEqual(created_post.title, 'Test Title')
        self.assertEqual(created_post.body, 'Test Body')


    def test_redirect_to_successfully_created_post(self):
        login = self.client.login(username='test_user', password='password')

        """
        Confirm that there are no created posts
        """
        self.assertEqual(models.Post.objects.count(), 0)

        form_data = {
            'title': 'Test Title',
            'body': 'Test Body',
        }

        response = self.client.post(reverse('blog:create_post'), form_data)

        """
        Confirm redirect and that there is now one created post
        """
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('blog:view_post', args=[models.Post.objects.last().slug]))
        self.assertEqual(models.Post.objects.count(), 1)


    def test_successfully_created_post_correct_template(self):
        login = self.client.login(username='test_user', password='password')

        """
        Confirm that there are no created posts
        """
        self.assertEqual(models.Post.objects.count(), 0)

        form_data = {
            'title': 'Test Title',
            'body': 'Test Body',
        }

        response = self.client.post(reverse('blog:create_post'), form_data, follow=True)

        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(str(response.context['user']), self.user.get_username())
        self.assertRedirects(response, reverse('blog:view_post', args=[models.Post.objects.last().slug]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(models.Post.objects.count(), 1)
        self.assertTemplateUsed(response, 'blog/view_post.html')



@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class BlogUserEditPostsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='test_user', password='password')


    def test_edit_post_redirect_to_login_if_not_authenticated(self):
        post = models.Post.objects.create(author_id=self.user, title='Test Title', body='Test body', pub_date=timezone.now(), slug=slugify('Test Title'))

        response = self.client.get(reverse('blog:edit_post', args=[post.slug]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/registration/login/?next=/blog/{post.slug}/edit_post/')


    def test_edit_post_view_if_authenticated_but_not_author(self):
        post = models.Post.objects.create(author_id=self.user, title='Test Title', body='Test body', pub_date=timezone.now(), slug=slugify('Test Title'))
        # new_user = get_user_model().objects.create_user(username='test_user2', password='password')
        second_user = get_user_model().objects.create_user(username='second_user', password='password2')

        login = self.client.login(username='second_user', password='password2')
        response = self.client.get(reverse('blog:edit_post', args=[post.slug]), follow=True)

        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(str(response.context['user']), second_user.get_username())

        self.assertRedirects(response, reverse('blog:view_post', args=[post.slug]))

        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "You aren't the author of this post")
        self.assertTemplateUsed(response, 'blog/view_post.html')


    def test_logged_in_edit_post_view_correct_template(self):
        post = models.Post.objects.create(author_id=self.user, title='Test Title', body='Test body', pub_date=timezone.now(), slug=slugify('Test Title'))

        login = self.client.login(username='test_user', password='password')
        response = self.client.get(reverse('blog:edit_post', args=[post.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), self.user.get_username())
        self.assertTemplateUsed(response, 'blog/edit_post.html')


    def test_blank_edit_post_form(self):
        form = forms.PostForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'title': ['This field is required.'],
            'body': ['This field is required.'],
        })


    def test_valid_edit_post_form(self):
        post = models.Post.objects.create(author_id=self.user, title='Test Title', body='Test body', pub_date=timezone.now(), slug=slugify('Test Title'))

        login = self.client.login(username='test_user', password='password')
        response = self.client.get(reverse('blog:edit_post', args=[post.slug]))

        form = forms.PostForm(instance=post)
        edited_post = form.save(commit=False)

        # self.assertTrue(form.is_valid())
        self.assertEqual(edited_post.title, post.title)
        self.assertEqual(edited_post.body, post.body)

        edited_post.title = 'New test title'
        edited_post.body = 'New test body'

        edited_post.save()

        self.assertEqual(edited_post.title, 'New test title')
        self.assertEqual(edited_post.body, 'New test body')


    def test_redirect_to_successfully_edited_post(self):
        post = models.Post.objects.create(author_id=self.user, title='Test Title', body='Test body', pub_date=timezone.now(), slug=slugify('Test Title'))

        login = self.client.login(username='test_user', password='password')

        form_data = {
            'title': 'New test title',
            'body': 'New test body'
        }

        response = self.client.post(reverse('blog:edit_post', args=[post.slug]), form_data)

        """
        Confirm redirect to edited post
        """

        self.assertEqual(response.status_code, 302)
        self.assertEqual(models.Post.objects.last().title, 'New test title')
        self.assertEqual(models.Post.objects.last().body, 'New test body')


    def test_successfully_edited_post_correct_template(self):
        post = models.Post.objects.create(author_id=self.user, title='Test Title', body='Test body', pub_date=timezone.now(), slug=slugify('Test Title'))

        login = self.client.login(username='test_user', password='password')

        form_data = {
            'title': 'New test title',
            'body': 'New test body'
        }

        response = self.client.post(reverse('blog:edit_post', args=[post.slug]), form_data, follow=True)

        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertRedirects(response, reverse('blog:view_post', args=[models.Post.objects.last().slug]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), self.user.get_username())
        self.assertEqual(models.Post.objects.last().title, 'New test title')
        self.assertEqual(models.Post.objects.last().body, 'New test body')
        self.assertTemplateUsed(response, 'blog/view_post.html')



@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class BlogUserDeletePostsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='test_user', password='password')


    def test_delete_post_view_http_get_redirect_to_login_if_not_authenticated(self):
        post = models.Post.objects.create(author_id=self.user, title='Test Title', body='Test body', pub_date=timezone.now(), slug=slugify('Test Title'))

        response = self.client.get(reverse('blog:delete_post', args=[post.slug]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/registration/login/?next=/blog/{post.slug}/delete_post/')


    def test_delete_post_view_http_get_if_authenticated_but_not_author(self):
        post = models.Post.objects.create(author_id=self.user, title='Test Title', body='Test body', pub_date=timezone.now(), slug=slugify('Test Title'))
        second_user = get_user_model().objects.create_user(username='second_user', password='password2')

        login = self.client.login(username='second_user', password='password2')
        response = self.client.get(reverse('blog:delete_post', args=[post.slug]), follow=True)

        self.assertEqual(str(response.context['user']), second_user.get_username())

        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertRedirects(response, reverse('blog:view_post', args=[post.slug]))

        # self.assertContains(response, "You aren't the author of this post")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/view_post.html')


    def test_delete_post_view_http_post_redirect_to_login_if_not_authenticated(self):
        post = models.Post.objects.create(author_id=self.user, title='Test Title', body='Test body', pub_date=timezone.now(), slug=slugify('Test Title'))

        response = self.client.post(reverse('blog:delete_post', args=[post.slug]))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/registration/login/?next=/blog/{post.slug}/delete_post/')


    def test_delete_post_view_http_post_if_authenticated_but_not_author(self):
        post = models.Post.objects.create(author_id=self.user, title='Test Title', body='Test body', pub_date=timezone.now(), slug=slugify('Test Title'))
        second_user = get_user_model().objects.create_user(username='second_user', password='password2')

        login = self.client.login(username='second_user', password='password2')
        response = self.client.post(reverse('blog:delete_post', args=[post.slug]), follow=True)

        self.assertEqual(str(response.context['user']), second_user.get_username())

        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertRedirects(response, reverse('blog:view_post', args=[post.slug]))
        # self.assertContains(response, "You aren't the author of this post")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/view_post.html')


    def test_delete_post_success(self):
        post = models.Post.objects.create(author_id=self.user, title='Test Title', body='Test body', pub_date=timezone.now(), slug=slugify('Test Title'))

        self.assertEqual(models.Post.objects.count(), 1)

        login = self.client.login(username='test_user', password='password')
        response = self.client.post(reverse('blog:delete_post', args=[post.slug]))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(models.Post.objects.count(), 0)


    def test_delete_post_success_correct_template(self):
        post = models.Post.objects.create(author_id=self.user, title='Test Title', body='Test body', pub_date=timezone.now(), slug=slugify('Test Title'))

        self.assertEqual(models.Post.objects.count(), 1)

        login = self.client.login(username='test_user', password='password')
        response = self.client.post(reverse('blog:delete_post', args=[post.slug]), follow=True)

        self.assertEqual(response.redirect_chain[0][1], 302)
        self.assertEqual(str(response.context['user']), self.user.get_username())
        self.assertEqual(models.Post.objects.count(), 0)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('blog:index'))
