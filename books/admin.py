from django.contrib import admin
from .models import *
# Register your models here.

# Book Admin For Admin Page
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn')


class AuthorAdmin(admin.ModelAdmin):
    pass


class BookAuthorAdmin(admin.ModelAdmin):
    pass


class BookReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookReview, BookReviewAdmin)