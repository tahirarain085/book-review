from django import forms 
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','description','genre','isbn','publication_date','average_rating']


        widgets = {
            'title' : forms.TextInput(attrs={"class": "form-control",'placeholder':'Enter Book Title'}),
            'author' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Author Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control','row':4, 'placeholder':'Write a Description'}),
            'isbn': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter ISBN'}),
            'genre': forms.Select(attrs={'class':'form-control','placeholder':'Select a Genre'}),
            'publication_date':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'average_rating' : forms.NumberInput(attrs={'class':'form-control','placeholder': 'Enter Rating'})
        }