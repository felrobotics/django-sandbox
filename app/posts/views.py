from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


# NOTE: Section 14 we changed the functions to classes
from django.views.generic import ListView, DetailView
from django.views import View

from .models import Post
from .forms import CommentForm

from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


# NOTE: first vews were created with functions
# namely, starting_page, posts and single_post
# Let's do the same below with classes
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


# http://127.0.0.1:8000/posts/my-first-post
# http://127.0.0.1:8000/posts/programming-is-fun
def single_post(request, slug):
    # post = Post.objects.filter(slug=slug) # better to use get, since is a single post
    # post = Post.objects.get(slug=slug) # But even better to use get_object_or_404
    post = get_object_or_404(Post, slug=slug)
    return render(
        request, "posts/post-detail.html", {"post": post, "post_tags": post.tags.all()}
    )


# http://127.0.0.1:8000/posts/with-class
class StartingPageView(ListView):
    template_name = "posts/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"  # template is using that name, instead of object

    # we need to modify some methods because we only fetch 3 posts
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


# http://127.0.0.1:8000/posts/with-class/list
class AllPostsView(ListView):
    template_name = "posts/posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"  # so is in the template
    # we do not need to overwrite theclass SinglePostDetailView(DetailView):
    template_name = "posts/posts.html"


# NOTE: without comments DetailView was nice, however to hangle to POST method required
# NOTE: by the comments we will use better View instead of DetailView


class SinglePostDetailView(DetailView):
    template_name = "posts/post-detail.html"
    model = Post

    # django will automatically will fetch by slug, is supported out of the box
    # it is supported primary key and slug
    # It will also automatically raise a 404 not found.
    # the tags are failing, so we need to provide some context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context


class SinglePostView(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id),
        }
        return render(request, "posts/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("single-post-view", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id),
        }
        return render(request, "posts/post-detail.html", context)


class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "posts/stored-posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts

        return HttpResponseRedirect("/posts/with-class/list")
