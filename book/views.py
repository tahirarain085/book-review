from django.shortcuts import render,redirect
from . forms import BookForm
from . models import Book
from django.contrib import messages

# Create your views here.

def book_create(request):
   
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Book Created Successfully")
            return redirect("book-create ")
    else:
        
        form = BookForm(request.POST)


    return render(request,'book/book_form.html',{'form':form})