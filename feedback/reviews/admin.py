from django.contrib import admin

from reviews.models import Review

# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("username", "ratings", "review_text")
    list_filter = ("ratings",)


admin.site.register(Review, ReviewAdmin)
