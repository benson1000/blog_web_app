from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from blogs.models import Post
from model_bakery import baker
from datetime import datetime

class TestViews(TestCase):
    def setUp(self):
        self.home = reverse('home')
        self.create_post_url = reverse('post-create')
        self.about_url = reverse('about')
        self.user = get_user_model().objects.create(name='John Mburu')
        self.user.save()
        self.blogs=Post.objects.create(
            title='Climate Change', content='There has been an increase in global warming', author=self.user,
        )
        self.blogs.save()

    def test_home_view_not_logged(self):
        response=self.client.get(self.home_url)
        self.assertEqual(response.status_code, 302)

    def test_home_view_has_information_fields(self):
        self.assertIsInstance(self.blogs.title, str)
        self.assertIsInstance(self.blogs.content, str)
        self.assertEqual(self.blogs.author.name, 'John Mburu')

    def test_home_has_timestamp(self):
        self.assertIsInstance(self.blogs.date_posted, datetime)

    def test_form_creation_validation(self):
        response = self.client.post(self.create_post_url, {'title': 'Climate Change',
                                                          'content':'There has been an increase in global warming'})
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.blogs.title, 'Climate Change')
        self.assertEqual(self.blogs.content, 'There has been an increase in global warming')
    
    def test_about_view(self):
        response = self.client.get(self.about_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/about.html')
