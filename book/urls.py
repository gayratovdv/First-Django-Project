from django.urls import path

from book.views import book_list, book_detail, all_authors, author_detail

app_name = 'books'

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/<int:id>/', book_detail, name='book_detail'),
    path('authors/', all_authors, name='all_authors'),
    path('authors/<int:id>/', author_detail, name='author_detail'),
]
