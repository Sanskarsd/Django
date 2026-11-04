from django.contrib import admin
from .models import Address, Book,Author, Country


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_filter = ("rating", "is_bestselling")
    list_display = ("title", "author", "rating", "is_bestselling", "price")


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)