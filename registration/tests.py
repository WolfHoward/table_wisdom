from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from registration.models import Item
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

class ItemModelTest(TestCase):

    def test_sasving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
