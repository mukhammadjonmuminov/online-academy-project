from django.contrib import admin
from .models import Book
from import_export.admin import ImportExportActionModelAdmin

@admin.register(Book)
class BookAdmin(ImportExportActionModelAdmin):
    search_fields = ('title', 'author')
    list_display = ('title', 'author', 'count')
    list_filter = ('author', )