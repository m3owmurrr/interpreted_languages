from django.urls import path
from django.contrib import admin
from . import views
from .views import adding_page, modify_Authors, add_Authors, add_books, add_authorsbook, draw_authors_table, \
    draw_books_table, draw_authorsbooks_table

urlpatterns = [
    path('', views.index),
    path('adding_page/', adding_page, name='adding_page'),
    path('admin/', admin.site.urls),
    path('modify_Authors/<int:Authors_id>/', modify_Authors, name='modify_Authors'),
    path('add_Authors/', add_Authors, name='add_Authors'),
    path('add_books/', add_books, name='add_books'),
    path('add_authorsbook/', add_authorsbook, name='add_authorsbook'),
    path('draw_authors_table/', draw_authors_table, name='draw_authors_table'),
    path('draw_books_table/', draw_books_table, name='draw_books_table'),
    path('draw_authorsbooks_table/', draw_authorsbooks_table, name='draw_authorsbooks_table'),
]
