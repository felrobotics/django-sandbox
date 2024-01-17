from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False
    )  # False so, nobody can edit it from the admin area
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=options, default="draft")

    tags = TaggableManager()

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post_single", args=[self.slug])
