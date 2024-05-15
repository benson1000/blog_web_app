"""Test for the blog models"""

from django.test import TestCase
from blogs.models import Post
#from model_bakery import baker
from django.urls import reverse, resolve


class ModelTests(TestCase):
    def setUp(self):
       self.blogs = baker.make('blogs.Post', title='john').pk

    def test_post_model(self):
        data=baker.make('blogs.Post', title='topic')
        self.assertEqual(isinstance(data, Post))
        self.assertEqual(data.title, 'topic')

    def test_url(self):
        res = Post.objects.get(id=self.blogs)
        response=self.client.post(reverse('post-detail', args=[res.pk, ]))
        self.assertEqual(response.status_code, 405)