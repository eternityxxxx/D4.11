from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect
from p_library.models import Book, Author, Publisher
from django.db.models import Count


def index(request):
    template = loader.get_template("index.html")
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }

    return HttpResponse(template.render(biblio_data, request))


def books_list(request):
    books = Book.objects.all()

    return HttpResponse(books)


def authors_list(request):
    authors = Author.objects.all()

    return HttpResponse(authors)


def publishers(request):
    template = loader.get_template("publisher.html")
    publishers = Publisher.objects.annotate(books_count=Count('book_publisher'))
    data = {
        "publishers": publishers, 
    }

    return HttpResponse(template.render(data))    


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def hello_message(request):
    message = 'Welcome to my library!'

    return HttpResponse(message)