from django.test import TestCase
from django.shortcuts import reverse
from django.conf import settings
from importlib import import_module
from django.http import HttpRequest
from app_profile import models, utils, views
from app_auth import models as auth_models

# Create your tests here.

class TestFriendApp(TestCase):

    def setUp(self):
        self.user1 = auth_models.User(npm='1', username='wisnu', angkatan=2016, role='dewa')
        self.user1.save()
        self.request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        session_key = None
        self.request.session = engine.SessionStore(session_key)
        self.request.session['user_login'] = {'npm': self.user1.npm}

    def test_profile_models(self):
        expert = models.Expertise(user=self.user1, expertise='ketawa', level='beginner')
        expert.save()
        self.assertEqual(expert.__str__(), 'ketawa')
        self.assertTrue(bool(models.Expertise.objects.all()))

    def test_profile_utils(self):
        riwayat = utils.__get_riwayat__()
        self.assertTrue(bool(riwayat))

        riwayat = utils.get_query_user_history(self.user1.npm)
        self.assertTrue(bool(riwayat))

    def test_profile_views(self):
        data = {}
        views.index(self.request, data)
        self.assertTrue(bool(data))
        self.assertTrue('user_riwayat' in data)

