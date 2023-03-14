from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        'sayfaadi': 'Anasayfa',
    }
    return render(request,'index.html',context)

def about(request):
    context = {
        'sayfaadi': 'Hakkinda',
    }
    return render(request,'about.html',context)