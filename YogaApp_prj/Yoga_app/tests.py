from django.test import TestCase
from .models import Post


class PostTests(TestCase):

    def test_str(self):
        test_title = Post(title='Blog Post - Pose of the Week')
        self.assertEqual(str(test_title), 'Blog Post - Pose of the Week')