from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import random

from loans.models import Book
from loans.forms import BookForm

SLOGAN_LIST = [
	"Having fun isn't hard when you've got a library card.",
	"Libraries make shhh happen.",
  	"Believe in your shelf.",
  	"Need a good read? We’ve got you cover to covered.",
  	"Check us out. And maybe one of our books too.",
  	"Get a better read on the world.",
]

def welcome(request):
    context = {'slogan': random.choice(SLOGAN_LIST)}
    return render(request, 'welcome.html', context)

def list_books(request):
    context = {'books': Book.objects.all()}
    return render(request, 'books.html', context)

def get_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        # Raise an Http404 error if the book is not found
        raise Http404(f"Could not find book with primary key {book_id}")
    else:
        context = {'book': book}
        return render(request, 'book.html', context)
    
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error(None, "It was not possible to save this book to the database.")
            else:
                path = reverse('list_books')
                return HttpResponseRedirect(path)
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

def update_book(request, book_id):
    # Retrieve the existing book, raise Http404 if it doesn't exist
    book = get_object_or_404(Book, pk=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)  # Bind form with the existing book instance
        if form.is_valid():
            form.save()
            path = reverse('list_books')
            return HttpResponseRedirect(path)
    else:
        form = BookForm(instance=book)  # Pre-fill the form with the existing book data

    context = {
        'form': form,
        'book': book,
        'is_update': True  # Flag to indicate that this is an update form
    }
    return render(request, 'update_book.html', context)

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        book.delete()  # Delete the book
        path = reverse('list_books')
        return HttpResponseRedirect(path)

    context = {
        'book': book,
    }
    return render(request, 'delete_book.html', context)