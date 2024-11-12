from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Book


# Create your views here.
def book_list(request):

    books = Book.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.add_message(
                    request, messages.ERROR,
                    'No search criteria entered'
                )
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            books = books.filter(queries)


    context = {
        'books': books,
        'search_term': query,
    }

    return render(request, 'books.html', context)


def view_book(request, uid):
    """
    View function to render book's info page
    """
    book = get_object_or_404(Book.objects.all(), uid=uid)

    return render(
        request,
        "view_book.html",
        {
            "book": book,
        },
    )