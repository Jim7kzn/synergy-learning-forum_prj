from django.shortcuts import render, redirect

# Create your views here.
from .models import Post, Comment


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
