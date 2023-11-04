
from rest_framework import serializers
from .models import Book, Review, Author

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['book','reviewer_name', 'content', 'rating']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['full_name', 'nick_name', 'date_of_birth', 'nationality', 'education', 'awards']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'published_date', 'isbn']

class BookListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'published_date', 'isbn']

class BookRestoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['pk','deleted','deleted_at']

class BookDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'published_date', 'isbn', 'reviews']

class UpdateBookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(write_only=True)
    class Meta:
        model = Book
        fields = ['title', 'author_name', 'genre', 'published_date', 'isbn']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author_name'] = instance.author.full_name if instance.author else None
        return representation
    
    def update(self, instance, validated_data):
        author_name = validated_data.pop('author_name', None)
        if author_name:
            author, created = Author.objects.get_or_create(full_name=author_name)
            instance.author = author
        return super().update(instance, validated_data)
