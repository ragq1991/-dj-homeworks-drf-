import datetime

from django.shortcuts import render
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


class DatePaginator:
    def __init__(self, list_date, page_date):
        self.list_date = list_date
        self.page_date = self.get_real_date(page_date)

    def get_real_date(self, page_date):
        page_date = datetime.datetime.strptime(page_date, '%Y-%m-%d').date()
        if page_date not in self.list_date:
            space = 365 * 3000
            page_date_real = page_date
            for dt in self.list_date:
                if abs((page_date - dt).days) < space:
                    space = abs((page_date - dt).days)
                    page_date_real = dt
            return page_date_real
        else:
            return page_date

    def has_next(self):
        if self.list_date.index(self.page_date) < len(self.list_date) - 1:
            return True
        else:
            return False

    def has_previous(self):
        if self.list_date.index(self.page_date) > 0:
            return True
        else:
            return False

    def previous_page_number(self):
        idx = self.list_date.index(self.page_date) - 1
        return self.list_date[idx]

    def next_page_number(self):
        idx = self.list_date.index(self.page_date) + 1
        return self.list_date[idx]
