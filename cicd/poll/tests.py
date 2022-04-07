from django.test import TestCase
from .models import Poll

# Create your tests here.

class ModelTesting(TestCase):

    def setUp(self):
        self.blog = Poll.objects.create(title='Test', author='Niko', slug='Test')

    def test_model_create(self):
        d = self.blog
        self.assertTrue(isinstance(d, Poll))