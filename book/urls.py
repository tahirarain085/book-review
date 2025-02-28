from django.urls import path
from . import views

urlpatterns = [
    path('book/new/',views.book_create,name='book-create')
]
