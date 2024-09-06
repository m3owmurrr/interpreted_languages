from django import forms
from .models import AuthorsBooks, Authors, Books

class AuthorsForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ['name', 'lastName', 'birthDate', 'birthCity']

class AuthorsBooksForm(forms.ModelForm):
    Authors = forms.ModelChoiceField(queryset=Authors.objects.all().values_list('name', flat=True), label='Имя Автора')
    Books = forms.ModelChoiceField(queryset=Books.objects.all().values_list('title', flat=True), label='Название Книги')

    class Meta:
        model = AuthorsBooks
        fields = ['Authors', 'Books']
        