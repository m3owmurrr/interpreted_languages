from django.contrib import admin
from .models import Authors, Books, AuthorsBooks

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'lastName','birthDate']  # Список отображаемых полей
    list_filter = ['birthDate']  # Фильтр по полю

class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'descr', 'genre', 'rate']  # Список отображаемых полей
    list_filter = ['rate']  # Фильтр по полю

class AuthorsBooksAdmin(admin.ModelAdmin):
    list_display = ['Authors_name', 'Books_title']  # Список отображаемых полей
    list_filter = ['Books_title']  # Фильтр по полю

admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(AuthorsBooks, AuthorsBooksAdmin)