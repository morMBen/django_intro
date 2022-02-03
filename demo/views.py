from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book


class Another(View):
    # books = Book.objects.all()  # select all books in our system
    # books = Book.objects.get(is_published=True) # Select only one
    books = Book.objects.filter(id=2)
    output = ''
    for book in books:
        output += f'We have {book.title} book in DB with id {book.id}<br>'

    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse('First message from views')
