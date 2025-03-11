from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse

# Create your models here.
class Book(models.Model):

    GENRE_CHOICES = [
        ('Fiction','FICTION'),
        ('Non-fiction','NON-FICTION'),
        ('Technology','TECHNOLOGY'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=20,choices=GENRE_CHOICES)
    isbn = models.CharField( "ISBN",max_length=15, unique = True, default="1")
    publication_date = models.DateField()
    average_rating = models.DecimalField(
        decimal_places= 1,
        max_digits=3,
        validators= [MinValueValidator(0), MaxValueValidator(5)],

        default=0
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"pk":self.pk})