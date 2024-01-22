from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(max_length=100, null=True)
    is_bestselling = models.BooleanField(default=False)
    # slug = models.SlugField(default="", null=False)  # orig code, but not so perfor
    # makes db_index in slug get_absolute_url search more efficient
    slug = models.SlugField(default="", null=False, db_index=True)

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])

        # return reverse("book_detail", kwargs={"id": self.id})
        # you can also use the following (explained in the course)
        # return reverse("book_detail", args=[self.id)]
        # you can also use self.pk
        # return reverse("book_detail", kwargs={"id": self.id})

    def save(self, *args, **kwargs):
        """Override save method to create the slug from title"""
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
