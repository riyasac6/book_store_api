from django.db import models
from django.utils import timezone
# Create your models here.

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=50, blank=True, null=True, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    education = models.CharField(max_length=50, blank=True, null=True)
    awards = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.full_name

class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def soft_delete(self):
        return self.update(deleted=True, deleted_at=timezone.now())

    def restore(self):
        return self.update(deleted=False, deleted_at=None)
    
class Book(models.Model):
    objects = SoftDeletionManager()
    
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)
    published_date = models.DateField()
    isbn = models.CharField(max_length=50, unique=True)
    deleted = models.BooleanField(default=False, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def undelete(self):
        self.deleted = False
        self.deleted_at = None
        self.save()

    def is_deleted(self):
        return self.deleted
    
    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f'Review for {self.book.title} by {self.reviewer_name}'