# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Book

def index(request):
    
    return render(request,'Books_app/index.html')

def submit_survey(request):
    if request.method == "POST":
        Book.objects.create(title_name=request.POST['title_name'], author_name= request.POST['author_name'],published_name= request.POST['published_name'], category_name= request.POST['category_name'], in_print= True)
        
        book = Book.objects.all()
        print request.POST
    return redirect('/result')
      
def result(request):
    context = {
        'books' : Book.objects.all()
    }
    return render(request, 'books_app/submitted.html', context)
