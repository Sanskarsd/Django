from django.shortcuts import render
from .models import Book



def book_outlet(request):
    book_list=Book.objects.all()
    return render(request,"book_outlet/book_outlet.html",{"books":book_list})

# Create your views here.
def book_detail(request,slug):
    book=Book.objects.get(slug=slug)
    return render(request,"book_outlet/book_detail.html",{"book":book})