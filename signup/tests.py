from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from registration.models import User
from registration.views import user_registration

class BasicInfoTest(TestCase):
    def test_uses_basic_info(self):
        response=self.client.get('/registration/basic_info/')
        self.assertTemplateUsed(response, 'basic_info.html')

        

# class UserRegistrationTest(TestCase):
#
#     def test_uses_user_registration(self):
#         response = self.client.get('/user_registration/')
#         self.assertTemplateUsed(response, 'user_registration.html')
#
#     def test_can_save_a_POST_request(self):
#         self.client.post('/user_registration/', data={
#             'discipline_text': 'User\'s discipline',
#             })
#
#         self.assertEqual(User.objects.count(), 1)
#         user_discipline = User.objects.first()
#         self.assertEqual(user_discipline.discipline, 'User\'s discipline')
#
#     def test_redirects_after_POST(self):
#         response = self.client.post('/user_registration/', data={
#             'discipline_text': 'User\'s discipline',
#         })
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response['location'], '/user_registration/')
#
#
#     def test_only_saves_items_when_necessary(self):
#         self.client.get('/user_registration/')
#         self.assertEqual(User.objects.count(), 0)
#
#     def test_displays_profile_info(self):
#         User.objects.create(discipline="Entrepreneur")
#
#         response = self.client.get('/user_registration/')
#
#         self.assertIn('Entrepreneur', response.content.decode())
# #        self.assertIn('The Rolling Stones', response.content.decode())
#
# class UserModelTest(TestCase):
#
#     def test_saving_and_retrieving_items(self):
#         first_item = User()
#         first_item.discipline = 'The first (ever) list item'
#         first_item.save()
#
#         second_item = User()
#         second_item.discipline = "Item the second"
#         second_item.save()
#
#         saved_items = User.objects.all()
#         self.assertEqual(saved_items.count(), 2)
#
#         first_saved_item = saved_items[0]
#         second_saved_item = saved_items[1]
#         self.assertEqual(first_saved_item.discipline, 'The first (ever) list item')
#         self.assertEqual(second_saved_item.discipline, 'Item the second')
