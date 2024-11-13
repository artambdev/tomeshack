from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Category, Book


# Create your views here.
def book_list(request):

    books = Book.objects.all()
    query = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            books = books.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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
    reviews = book.replies.all().order_by("created_on")
    num_reviews = book.reviews.filter(hidden=False).count()

    return render(
        request,
        "view_book.html",
        {
            "book": book,
            "reviews": reviews,
            "num_reviews": num_reviews,
        },
    )