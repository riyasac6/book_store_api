from django.urls import path
from .views import *

urlpatterns = [
    
	path('books/', BookListView.as_view(), name='book-list'),
	path('books/create/', BookCreateView.as_view(), name='book-create'),
	path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
	path('books/<int:pk>/update/', UpdateBookView.as_view(), name='book-update'),
	path('books/<int:pk>/soft-delete/', SoftDeleteBookView.as_view(), name='book-soft-delete'),
	path('books/<int:pk>/restore/', RestoreBookView.as_view(), name='book-restore'),

	path('author/', AuthorListView.as_view(), name='author-list'),
	path('author/create/', AuthorCreateView.as_view(), name='author-create'),
	path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-list'),
 
	path('reviews/', ReviewListView.as_view(), name='review-list'),
	path('review/create/', ReviewCreateView.as_view(), name='review-create'),
	path('review/<int:pk>/update/', UpdateBookView.as_view(), name='review-update'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),

]