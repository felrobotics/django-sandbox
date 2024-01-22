from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book
from django.db.models import Avg, Max, Min

# Create your views here.


def index(request):
    books = Book.objects.all()  # origional by id
    books = Book.objects.all().order_by("title")  # asc order
    books = Book.objects.all().order_by("-title")  # desc order
    books = Book.objects.all().order_by("-rating")  # desc order
    num_books = books.count()
    avg_books = books.aggregate(Avg("rating"))
    #                                               -> context
    # return render(request, "book_outlet/index.html", {"books": books}) # original
    # Now, modify it to compute agg
    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "total_number_of_books": num_books,
            "average_rating": avg_books,
        },
    )


def book_detail(request, slug):
    # def book_detail(request, id): # before slug we used id
    #  This pattern is so common that can be replaced with get_object_or_404,
    # therefore I will comment it
    # try:
    #     book = Book.objects.get(pk=id)
    # except Exception:
    #     raise Http404()

    # above code can be replaced with
    # book = get_object_or_404(Book, pk=id) # before we added the slug, we used id
    book = get_object_or_404(Book, slug=slug)

    return render(
        request,
        "book_outlet/book_detail.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestselling": book.is_bestselling,
        },
    )
