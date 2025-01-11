from django.shortcuts import render

from .admin import AuthorAdmin
from .models import BookModel, AuthorModel


def book_list(request):
#     books = BookModel.objects.filter(price__lte=500)
#     books = BookModel.objects.filter(discount__isnull=True)
#     books = BookModel.objects.filter(author__name__startswith='A')
    books = BookModel.objects.filter(author__age__gte=35).filter(author__age__lte=70)
    return render(request, 'index.html', {'books': books})

def book_detail(request, id):
    book = BookModel.objects.get(id=id)
    return render(request, 'details.html', {'book': book})


def all_authors(request):
    authors = AuthorModel.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'authors.html', context)


def author_detail(request, id):
    author = AuthorModel.objects.get(id=id)
    books = author.books.all()

    context = {
        'author': author,
        'books': books
    }

    return render(request, 'author_book.html', context)


