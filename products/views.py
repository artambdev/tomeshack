import uuid
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Category, Book, Review
from .forms import ReviewForm


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

    return render(request, 'products/books.html', context)


def view_book(request, uid):
    """
    View function to render book's info page
    """
    book = get_object_or_404(Book.objects.all(), uid=uid)
    reviews = book.reviews.all().order_by("created_on")
    num_reviews = book.reviews.filter(hidden=False).count()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.slug = uuid.uuid4().hex.upper()
            new_review.review_of = book
            new_review.author = request.user
            new_review.hidden = False
            new_review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review created successfully'
            )
            return HttpResponseRedirect(
                reverse('view_book', args=[book.uid])
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'There was an error creating your review'
            )

    review_form = ReviewForm()

    return render(
        request,
        "products/view_book.html",
        {
            "book": book,
            "reviews": reviews,
            "num_reviews": num_reviews,
            "review_form": review_form,
        },
    )