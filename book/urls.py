from django.urls import path
from . import views

urlpatterns = [
    path('',views.book_list,name="book-list"),
    path('book/<int:pk>/',views.book_deatil,name="book-detail"),
    path('book/new/',views.book_create,name='book-create'),
    path('book/<int:pk>/edit/',views.book_update,name="book-update"),
    path('book/<int:pk>/delete/',views.book_delete,name="book-delete"),
]
