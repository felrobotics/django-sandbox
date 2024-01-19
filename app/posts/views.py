from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


# http://127.0.0.1:8000/posts/
def starting_page(request):
    return render(request, "posts/index.html")


# http://127.0.0.1:8000/posts/list
def posts(request):
    return render(request, "posts/posts.html")


def single_post(request, slug):
    return render(request, "posts/post.html")
