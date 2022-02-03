from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'is_published']
    list_display = ['title', 'description', 'price']
    list_filter = ['published']
    search_fields = ['title', 'description']
