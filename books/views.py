from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Books
def index(request):
    books = Books.objects.all()
    a = {
        'data2': books, 
        'title': 'Каталог'
    }
    return render(request, 'books/index.html', a)