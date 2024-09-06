from django.shortcuts import render, redirect, get_object_or_404
from .models import Authors, Books, AuthorsBooks
from .forms import AuthorsForm, AuthorsBooksForm

def index(request):
    authors = Authors.objects.all()
    return render(request, 'main/index.html', {'authors': authors})

def adding_page(request):
    form = AuthorsBooksForm()
    return render(request, 'main/adding_page.html', {'form': form})

def add_Authors(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastName = request.POST.get('lastName')
        birthDate = request.POST.get('birthDate')
        birthCity = request.POST.get('birthCity')

        Authors.objects.create(name=name, lastName=lastName, birthDate=birthDate, birthCity=birthCity)

        return redirect('adding_page')

    return render(request, 'main/index.html')

def modify_Authors(request, Authors_id):
    authors = get_object_or_404(Authors, id=Authors_id)

    if request.method == 'POST':
        form = AuthorsForm(request.POST, instance=authors)
        if form.is_valid():
            form.save()
            return redirect('../../')  # Перенаправление после успешной модификации
    else:
        form = AuthorsForm(instance=authors)

    return render(request, 'main/modify_Authors.html', {'form': form, 'authors': authors})

def add_books(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        descr = request.POST.get('descr')
        genre = request.POST.get('genre')
        rate = request.POST.get('rate')

        Books.objects.create(title=title, descr=descr, genre=genre, rate=rate)

        return redirect('adding_page')

    return render(request, 'main/index.html')

def add_authorsbook(request):
    if request.method == 'POST':
        AuthorsBooks.objects.create(Authors_name=request.POST.get('Authors'),Books_title=request.POST.get('Books'))
        return redirect('adding_page')
    else:
        form = AuthorsBooksForm()

    return render(request, 'main/index.html', {'form': form})

def draw_authors_table(request):
    authors = Authors.objects.all()
    return render(request, 'main/authors_table.html', {'authors': authors})

def draw_books_table(request):
    books = Books.objects.all()
    return render(request, 'main/books_table.html', {'books': books})

def draw_authorsbooks_table(request):
    authorsbooks = AuthorsBooks.objects.all()
    return render(request, 'main/authorsbooks_table.html', {'authorsbooks': authorsbooks})