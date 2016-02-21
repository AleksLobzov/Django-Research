from django.shortcuts import get_object_or_404, render

from .models import Book, Author, Publisher

from django.http import HttpResponse

import json


def index(request):
  latest_book_list = Book.objects.order_by('-publication_date')[:10]
  
  book_by_publisher_piechart_data = [[str(publisher), len(Book.objects.all().filter(publisher=publisher))] for publisher in Publisher.objects.all()]
  
  context = {'latest_book_list': latest_book_list, 'book_by_publisher_piechart_data': book_by_publisher_piechart_data}
  return render(request, 'books/index.html', context)


def book_detail(request, book_id):
  book = get_object_or_404(Book, pk=book_id)
  return render(request, 'books/book_detail.html', {'book': book})


def author_detail(request, author_id):
  author = get_object_or_404(Author, pk=author_id)
  books = Book.objects.all().filter(authors=author)
  return render(request, 'books/author_detail.html', {'author': author, 'books': books})

def chart1_data(request):
  a = [{'key':str(author),'value':len(Book.objects.all().filter(authors=author))} for author in Author.objects.all()]
  json_data = json.dumps(a)
  return HttpResponse(json_data, content_type='application/json')
