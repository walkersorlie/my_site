from django.test import RequestFactory, TestCase, override_settings
from django.urls import reverse
from django.utils import timezone
from my_cv.models import Education, ExperienceOrOutreach
from . import models
from .views import IndexView



@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class HomepageIndexViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = RequestFactory()
        cls.about_content = models.AboutContent.objects.create(body="About content test body", last_edited=timezone.now())
        # cls.blurb = models.HomepageBlurb.objects.create(body="Homepage blurb test body", last_edited=timezone.now())


    def test_no_about_content_block_middleware(self):
        request = self.factory.get(reverse('homepage:index'))
        response = IndexView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "About content test body")


    def test_yes_about_content_block_middleware(self):
        request = self.factory.get(reverse('homepage:index'))
        request.about_content_block = self.about_content

        response = IndexView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About content test body")


    def test_no_homepage_blurb_block(self):
        request = self.factory.get(reverse('homepage:index'))
        view = IndexView()
        view.setup(request)

        queryset = view.get_queryset()
        self.assertEqual(queryset, None)


    def test_yes_homepage_blurb_block(self):
        blurb = models.HomepageBlurb.objects.create(body="Homepage blurb test body", last_edited=timezone.now())
        request = self.factory.get(reverse('homepage:index'))
        response = IndexView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Homepage blurb test body")


    def test_education_experience_context_list_empty(self):
        request = self.factory.get(reverse('homepage:index'))
        view = IndexView()
        view.setup(request)

        view.object_list = view.get_queryset()
        context = view.get_context_data()
        self.assertIn('edu_exp_list', context)

        self.assertQuerysetEqual(context['edu_exp_list'], [])


    def test_education_experience_context_list_empty_template_response(self):
        request = self.factory.get(reverse('homepage:index'))
        response = IndexView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There is no education or experience information available")


    def test_education_experience_context_list_not_empty(self):
        education = Education.objects.create(name="Education name", location="Here", start_date=timezone.now(), description="Education description")
        experience = ExperienceOrOutreach.objects.create(
            name="Experience name", position_title="Position", location="Here", current_position=True, start_date=timezone.now(),
            description="Experience description", is_outreach=False)

        self.assertEqual(Education.objects.count(), 1)
        self.assertEqual(ExperienceOrOutreach.objects.count(), 1)

        request = self.factory.get(reverse('homepage:index'))
        view = IndexView()
        view.setup(request)

        view.object_list = view.get_queryset()
        context = view.get_context_data()
        self.assertIn('edu_exp_list', context)
        self.assertEqual(len(context['edu_exp_list']), 2)


    def test_education_experience_context_list_not_empty_template_response(self):
        education = Education.objects.create(name="Education name", location="Here", start_date=timezone.now(), description="Education description")
        experience = ExperienceOrOutreach.objects.create(
            name="Experience name", position_title="Position", location="Here", current_position=True, start_date=timezone.now(),
            description="Experience description", is_outreach=False)

        self.assertEqual(Education.objects.count(), 1)
        self.assertEqual(ExperienceOrOutreach.objects.count(), 1)

        request = self.factory.get(reverse('homepage:index'))
        response = IndexView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "There is no education or experience information available")
