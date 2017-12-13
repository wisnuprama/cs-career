from django.test import TestCase
from app_service import utils, models, views
# Create your tests here.


class TestAppService(TestCase):

    def setUp(self):
        self.public = models.PublicAccess(email='hehe@hehe.com')

    def test_models(self):
        self.assertTrue(self.public.__str__())
        self.assertEqual(self.public.__str__(), self.public.email)

    def test_utils(self):
        pass