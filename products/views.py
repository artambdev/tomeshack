from django.shortcuts import render
from .models import Book

# Create your views here.
def book_list(request):

    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'books.html', context)


def view_post(request, title):
    """
    View function to render book's info page
    """
    book = get_object_or_404(Book.objects.all(), title=title)

    return render(
        request,
        "products/view_book.html",
        {
            "book": book,
        },
    )