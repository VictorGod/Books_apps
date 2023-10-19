from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author

class BookApiTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(title='Test Book')
        self.book.authors.add(self.author)
        self.client = APIClient()

    def test_get_books_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  

