from django.test import TestCase, Client
from django.shortcuts import reverse
from django.http import HttpRequest
from app_friend import models, utils, views
from app_auth import models as auth_models
from django.conf import settings
from importlib import import_module

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

    def test_model_friend(self):
        user2 = auth_models.User(npm='2', username='wkwk', angkatan=2011, role='dewa2')
        user2.save()
        friend = models.Friendship(user1=self.user1, user2=user2)
        friend.save()
        self.assertEqual(friend.__str__(), self.user1.npm + ' - ' + user2.npm)

    def test_utils_friend(self):
        n = utils.get_number_of_friend(self.user1)
        self.assertEqual(n, 0)
        user2 = auth_models.User(npm='2', username='lolololol', angkatan=2011, role='dewa2')
        user2.save()

        friend = models.Friendship(user1=self.user1, user2=user2)
        friend.save()

        serr = utils.serialize_friendship(friend)
        self.assertTrue('user1' in serr)
        self.assertTrue('user2' in serr)

        query = utils.get_user_friends(user=self.user1)
        self.assertTrue(bool(query))

        user3 = auth_models.User(npm='3', username='lol', angkatan=1900, role='mahasiswa')
        user3.save()
        friendship = utils.insert_new_friend_to_database(self.user1, user3)
        self.assertEqual(friendship.user1, self.user1)

        query = utils.get_all_mahasiswa_except(self.user1)
        self.assertTrue(len(query), 2)

    def test_views_friend(self):
        data = {}
        views.index(self.request, data)
        self.assertTrue('number_of_friend' in data)
        self.request.method = 'GET'
        resp = views.get_all_friend_candidate(self.request)
        self.assertEqual(200, resp.status_code)

        user3 = auth_models.User(npm='3', username='lol', angkatan=1900, role='mahasiswa')
        user3.save()
        self.request.method = 'POST'
        self.request.POST['npm'] = user3.npm
        resp = views.post_new_friend(self.request)
        self.assertEqual(resp.status_code, 200)