from django.test import TestCase

from .models import Author, Book, Publisher


class AuthorMethodTests(TestCase):

  
  def test_author_name(self):
    '''
    Author.__str__() should return correct string with author’s first and last names
    '''
    a = Author(salutation='Sr.',
               first_name='John',
               last_name='Smith',
               email='john.smith@gmail.com')
    self.assertEqual(str(a), 'John Smith')


  def test_book_title(self):
    '''
    Book.__str__() should return correct string with book title
    '''
    b = Book(title='Marina')
    self.assertEqual(str(b), 'Marina')


  def test_publisher_name(self):
    '''
    Publisher.__str__() should return correct string with publisher name
    '''
    p = Publisher(name='Mann, Ivanov, Ferber')
    self.assertEqual(str(p), 'Mann, Ivanov, Ferber')
