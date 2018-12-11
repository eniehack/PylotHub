from django.test import TestCase
from accounts.models import User


class PlotViewTests(TestCase):

    def test_get_index(self):
        response = self.client.get('/plots/')
        self.assertEqual(response.status_code, 200)

    def test_post_new_authenticated(self):
        self.client.force_login(User.objects.create_user('tester'))
        response = self.client.post('/plots/new', {'title': 'test', 'content': 'test'})
        self.assertEqual(response.status_code, 200)