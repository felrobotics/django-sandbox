from django.contrib import admin

from .models import Author, Post, Tag

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = (
        "author",
        "tags",
        "date",
    )

    # modify the display table in admin/
    list_display = ("title", "author", "date")

    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
