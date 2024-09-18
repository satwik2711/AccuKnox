from django.test import TestCase, Client
from django.urls import reverse
from .models import MyModel

class SignalAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_model(self):
        url = reverse('create_model')
        response = self.client.post(url, {'name': 'Test Model'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json())

    def test_trigger_request_finished(self):
        url = reverse('trigger_request_finished')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Request finished')

    def test_create_model_with_related(self):
        url = reverse('create_model_with_related')
        response = self.client.post(url, {'name': 'Parent Model'}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.json())
        # Check if related object was created
        self.assertEqual(MyModel.objects.count(), 2)