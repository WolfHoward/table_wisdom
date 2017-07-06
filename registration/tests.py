from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from registration.views import user_registration


class HomePageTest(TestCase):

    def test_root_url_resolves_to_user_registration(self):
        found = resolve('/user_registration/')
        self.assertEqual(found.func, user_registration)

    def test_uses_user_registration(self):
        response = self.client.get('/user_registration/')
        self.assertTemplateUsed(response, 'user_registration.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/user_registration/', data={'discipline_text': 'A new discipline'})
        self.assertIn('A new discipline', response.content.decode())
        self.assertTemplateUsed(response, 'user_registration.html')
