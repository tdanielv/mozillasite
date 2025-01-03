from django.contrib import admin

from .models import Author, Book, BookInstance, Genre, Language

class BookInstanceInLine(admin.TabularInline):
    model = BookInstance

class BookInline(admin.TabularInline):
    model = Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'summary', 'display_genre')
    list_filter = ('title', 'author')
    inlines = [BookInstanceInLine]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'id', 'due_back', 'status')
    list_filter = ('due_back', 'status', 'book')
    fieldsets = (
        ('Основная информация', {
            'fields':('book', ('id', 'imprint'))}),
        ('Доступность книги', {
            'fields':(('due_back', 'status'),)
        })
    )
    
admin.site.register(Language)

admin.site.register(Genre)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = [('first_name', 'last_name'), ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]
