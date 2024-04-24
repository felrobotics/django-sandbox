from django.contrib import admin

from .models import Author, Post, Tag, Comment

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


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")
    # list_filter = (

    # )


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
