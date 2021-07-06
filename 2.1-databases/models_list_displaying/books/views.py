import datetime

from django.shortcuts import render

from . import DatePaginator
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    context = {
        'books': books
    }
    return render(request, template, context)


def book_view(request, pub_date):
    template = 'books/book.html'
    books = Book.objects.all().order_by('pub_date')
    date = pub_date
    list_of_date = []
    for book in books:
        list_of_date.append(book.pub_date)
    page = DatePaginator(list_of_date, date)
    book = Book.objects.filter(pub_date=page.page_date).first()
    context = {
        'book': book,
        'page': page
    }
    return render(request, template, context)

