from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}({self.code})"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        to=Address, on_delete=models.CASCADE, null=True
    )  # one to one

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"pk": self.pk})


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    # author = models.CharField(max_length=100, null=True) // original string
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books"
    )
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    #  Lets show other option, this one will prepoluate the slug in the admin/
    slug2 = models.SlugField(default="", blank=True, null=False, db_index=True)
    # many to many creates behinds the scenes a 3rd mapping table
    published_countries = models.ManyToManyField(to=Country, related_name="books")

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
