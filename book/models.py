from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction','FICTION'),
        ('non-fiction','NON-FICTION'),
        ('technology','TECHNOLOGY')
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField( "ISBN",max_length=15, unique = True)
    publication_date = models.DateField()
    average_rating = models.DecimalField(
        decimal_places= 2,
        max_digits=3,
        validators= [MinValueValidator(0), MaxValueValidator(5)],

        default=0
    )
    created_at = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absoulte_url(self):
        return reverse("book-title", kwargs={"pk":self.pk})