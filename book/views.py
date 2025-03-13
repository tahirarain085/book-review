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
            return redirect("book-list")
    else:
        
        form = BookForm()


    return render(request,'book/book_form.html',{'form':form})

def book_list(request):
    genre = request.GET.get('genre')
    if genre:
        books = Book.objects.filter(genre=genre).order_by('-created_at')
    else:

        books = Book.objects.all().order_by('-created_at')
    return render(request,'book/book_list.html',{"books":books})

def book_deatil(request,pk):
    book = Book.objects.get(pk=pk)
    return render(request,'book/book_detail.html',{"book":book})

def book_update(request,pk):
    book = Book.objects.get(pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            messages.success(request,"Book Updated Successfully")
            return redirect("book-list")
    else:
        form = BookForm(instance=book)

    return render(request,'book/book_form.html',{'form':form})
def book_delete(request,pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    messages.success(request,"Book Deleted Successfully!..")
    return redirect('book-list')

    


    