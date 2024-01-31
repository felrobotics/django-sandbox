from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Post

# Create your views here.


# http://127.0.0.1:8000/posts/
def starting_page(request):
    # django is smart and will not query all objects, but slices to fetch
    # first 3 elements in a single sql query
    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(
        request,
        "posts/index.html",
        {"posts": latest_posts},
    )


# http://127.0.0.1:8000/posts/list
def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(
        request,
        "posts/posts.html",
        {"all_posts": all_posts},
    )


def single_post(request, slug):
    # post = Post.objects.filter(slug=slug) # better to use get, since is a single post
    # post = Post.objects.get(slug=slug) # But even better to use get_object_or_404
    post = get_object_or_404(Post, slug=slug)
    return render(
        request, "posts/post-detail.html", {"post": post, "post_tags": post.tags.all()}
    )
