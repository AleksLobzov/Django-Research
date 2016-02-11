from django.shortcuts import get_object_or_404, render

from .models import Book, Author


def index(request):
  latest_book_list = Book.objects.order_by('-publication_date')[:10]
  context = {'latest_book_list': latest_book_list}
  return render(request, 'books/index.html', context)


def book_detail(request, book_id):
  book = get_object_or_404(Book, pk=book_id)
  return render(request, 'books/book_detail.html', {'book': book})


def author_detail(request, author_id):
  author = get_object_or_404(Author, pk=author_id)
  books = Book.objects.all().filter(authors=author)
  return render(request, 'books/author_detail.html', {'author': author, 'books': books})