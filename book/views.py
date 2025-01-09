from django.shortcuts import render
from .models import BookModel

def book_list(request):
    books = BookModel.objects.order_by('-pk')
    return render(request, 'index.html', {'books': books})

def book_detail(request, id):
    book = BookModel.objects.get(id=id)
    return render(request, 'details.html', {'book': book})
