from django.db import models

class Book(models.Model):
    STATUS_CHOICES = [
        ('reading', 'Reading'),
        ('completed', 'Completed'),
        ('wishlist', 'Wishlist'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    pages_read = models.PositiveIntegerField(default=0)
    total_pages = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True)
    rating = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
