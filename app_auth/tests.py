import environ
from django.shortcuts import reverse
from django.test import TestCase, Client

from app_auth import models
from app_auth import utils
from .csui_helper import *

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env('.env')


# Create your tests here.
class TestAppAuth(TestCase):
    def setUp(self):
        self.username = env('SSO_USERNAME')
        self.password = env('SSO_PASSWORD')
        self.user = models.User(npm='1606918055', angkatan='2016', role='Mahasiswa',
                                username='hehe')
        self.user.save()

    def test_auth_csuihelper(self):

        access_token = get_access_token(self.username, self.password)
        self.assertNotEqual(access_token, None)

        try:
            access_token_non_sso = get_access_token('hehe', 'hehe')
        except:
            pass

        # hehe hehe
        self.assertEqual(get_client_id(), get_client_id())
        self.assertNotEqual(verify_user(access_token), None)
        self.assertNotEqual(get_user_data(access_token, '1606918055'), None)

    def test_auth_model(self):
        self.assertEqual(self.user.__str__(), '1606918055')
        self.assertEqual('1606918055', self.user.get_npm())

        data = {
            'first_name': 'Wisnu',
            'last_name': 'Prama',
        }

        self.user.set_user_data(**data)
        self.user.save()
        self.assertEqual(self.user.first_name, data['first_name'])
        self.assertEqual(self.user.last_name, data['last_name'])

    def test_auth_utils(self):
        ser_user = utils.serialize_user(user=self.user)
        self.assertTrue('full_name' in ser_user)
        self.assertTrue('username' in ser_user)
        self.assertTrue('npm' in ser_user)
        self.assertTrue('expertise' in ser_user)

        list_permission = utils.get_permission_for_sso_user()
        self.assertEqual(len(list_permission), 12)

        group_sso = utils.get_or_create_sso_group()
        self.assertEqual(group_sso.name, utils.SSO_GROUP_NAME)
        from django.contrib.auth.models import Group
        self.assertEqual(Group.objects.filter(name=utils.SSO_GROUP_NAME).count(), 1)

        self.assertTrue(utils.check_user_existence(npm='1606918055'))
        d = dict()
        self.assertFalse(utils.check_user_existence(**d))

        same_user = utils.get_or_create_user(npm='1606918055')
        self.assertEqual(same_user.get_npm(), self.user.get_npm())
        create_other = utils.get_or_create_user(npm='160606', username='user', angkatan=2014, role='dewa')
        self.assertEqual(create_other.npm, '160606')
        self.assertEqual(create_other.username, 'user')
        self.assertEqual(create_other.angkatan, 2014)
        self.assertEqual(create_other.role, 'dewa')

        self.assertEqual(utils.get_except_user_queryset(npm='1606').count(), 2)
        self.assertEqual(utils.get_except_user_queryset(angkatan=2014).count(), 1)
        self.assertEqual(utils.get_except_user_queryset(npm='1606918055').count(),
                         utils.get_user_queryset().count() - 1)

    def test_auth_utils(self):
        # LOGIN
        resp = Client().get(reverse('auth:login'))
        self.assertEqual(resp.status_code, 400)
        resp = Client().post(reverse('auth:login'), data={'username': 'hehe', 'password': 'hehe'},
                             follow=True)
        self.assertEqual(resp.status_code, 200)
        resp = Client().post(reverse('auth:login'), data={'username': self.username, 'password': self.password})
        self.assertEqual(resp.status_code, 302)

        # LOGOUT
        resp = Client().post(reverse('auth:logout'))
        self.assertEqual(resp.status_code, 400)
        resp = Client().get(reverse('auth:logout'))
        self.assertEqual(resp.status_code, 302)
