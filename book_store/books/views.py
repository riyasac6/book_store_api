from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from .models import Book, Author, Review
from .serializers import *
from rest_framework.response import Response

"""
1. Retrieve All Books with Filtering and Pagination (Read): 
	* Implement an endpoint that allows users to retrieve a list of all books
	* with filtering options (e.g., by author, genre, publication year)
	* and pagination for large result sets. 
"""
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    
    def get_queryset(self):
        queryset = Book.objects.filter(deleted=False).all().order_by('id')
        author = self.request.query_params.get('author')
        genre = self.request.query_params.get('genre')
        published_year = self.request.query_params.get('published_year')

        if author:
            queryset = queryset.filter(author=author)
        if genre:
            queryset = queryset.filter(genre=genre)
        if published_year:
            queryset = queryset.filter(published_date__year=published_year)
        return queryset

"""        
2. Retrieve a Single Book with Related Data (Read): 
	* Implement an endpoint that allows users to retrieve details for a single book by its unique identifier,
	* including related data like reviews 
	* and author details. 
"""
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

"""
3. Create a New Book (Create): 
    * Implement an endpoint that allows users to create a new book by providing the book's title, author, ISBN, and other relevant information.
    * Include validation to ensure that the ISBN is unique.
"""
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        author_name = request.data.get('author_name')
        if author_name:
            author_obj, created = Author.objects.get_or_create(full_name=author_name)
            book_data = request.data.copy()
            book_data['author'] = author_obj.id
            book_data['deleted'] = False
            serializer = self.get_serializer(data=book_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(book_data)
            book_data.pop('author', None)
            book_data.pop('deleted', None)
            return Response(book_data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"author_name": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
"""
4. Update a Book with Transactions (Update): 
    * Implement an endpoint that allows users to update the details of an existing book, including its related data.
    * Utilize database transactions to ensure data consistency during updates.
"""
class UpdateBookView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = UpdateBookSerializer

class SoftDeleteBookView(generics.DestroyAPIView):
    queryset = Book.objects.filter(deleted=False)
    serializer_class = BookSerializer

    def perform_destroy(self, instance):
        instance.delete()  # Soft delete the book
        return Response({"message": "Book soft deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class RestoreBookView(generics.UpdateAPIView):
    queryset = Book.objects.filter(deleted=True).all()
    serializer_class = BookRestoreSerializer
    
    def perform_update(self, serializer):
        serializer.instance.undelete()  # Restore the soft-deleted book
        return Response({"message": "Book restored successfully."}, status=status.HTTP_200_OK)
    
class AuthorCreateView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    def get_queryset(self):
        queryset = Author.objects.all().order_by('id')
        full_name = self.request.query_params.get('full_name')
        nick_name = self.request.query_params.get('nick_name')
        nationality = self.request.query_params.get('nationality')

        if full_name:
            queryset = queryset.filter(full_name=full_name)
        if nick_name:
            queryset = queryset.filter(nick_name=nick_name)
        if nationality:
            queryset = queryset.filter(nationality=nationality)
        return queryset

class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer