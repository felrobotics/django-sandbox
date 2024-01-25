from django.contrib import admin

from .models import Address, Author, Book, Country

# Register your models here.
# admin.site.register(Book) # simple registration, but we would like to config more


# This allows for a better customization and overwriting
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    prepopulated_fields = {"slug2": ("title",)}
    list_filter = ("rating",)
    list_display = ("title", "author")


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)
admin.site.register(Country)
