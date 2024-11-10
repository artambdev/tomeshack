from django.shortcuts import render
from .models import Book

# Create your views here.
def book_list(request):

    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'products/books.html', context)