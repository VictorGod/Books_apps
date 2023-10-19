from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author

class AuthorApiTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Test Author')
        self.client = APIClient()

    def test_get_authors_list(self):
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)  
