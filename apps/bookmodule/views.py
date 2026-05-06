from django.shortcuts import render
from django.db.models import Q
from .models import *
from django.db.models import Count, Sum, Avg, Max, Min
from django.db import models
from django.db.models import Count
from .models import Student
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Publisher, Author
from .forms import BookForm

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, "bookmodule/list_books.html")

def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")

def html5_links(request):
    return render(request, 'bookmodule/html5_links.html')

def html5_text_formatting(request):
    return render(request, 'bookmodule/html5_text_formatting.html')

def html5_listing(request):
    return render(request, 'bookmodule/listing.html')

def tables_page(request):
    return render(request, 'bookmodule/tables.html')

def search_books(request):
    return render(request, 'bookmodule/search.html')
def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False

            if isTitle and string in item['title'].lower():
                contained = True

            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            
            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def add_books(request):
    if Book.objects.count() == 0:  # إذا ما فيه بيانات
        Book.objects.create(title='AI and Data Science', author='Ali', price=150, edition=3)
        Book.objects.create(title='Python and Django', author='Sara', price=120, edition=2)
        Book.objects.create(title='Algorithms and Data Structures', author='Khalid', price=200, edition=4)

    return render(request, 'bookmodule/index.html')

    return render(request, 'bookmodule/index.html')
def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


def complex_query(request):
    mybooks = Book.objects.filter(
        author__isnull=False,
        title__icontains='and',
        edition__gte=2
    ).exclude(price__lte=100)[:10]

    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/task1.html', {'books': books})

def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & 
        (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3(request):
    books = Book.objects.filter(
        Q(edition__lte=3) & 
        ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task3.html', {'books': books})


def task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})

def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})
    

def task7(request):
    data = Student.objects.values('address__city').annotate(count=Count('id'))
    return render(request, 'bookmodule/task7.html', {'data': data})

def Task1(request):
    books = Book.objects.all()
    total_quantity = sum(book.quantity for book in books)

    for book in books:
        book.availability = (book.quantity / total_quantity * 100) if total_quantity else 0

    return render(request, 'bookmodule/Task1.html', {'books': books})

def Task2(request):
    publishers = Publisher.objects.annotate(
        total_stock=Sum('book__quantity')
    )
    return render(request, 'bookmodule/Task2.html', {'publishers': publishers})

def Task3(request):
    publishers = Publisher.objects.annotate(
        oldest_book=Min('book__pubdate')
    )
    return render(request, 'bookmodule/Task3.html', {'publishers': publishers})

def Task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/Task4.html', {'publishers': publishers})

def Task5(request):
    publishers = Publisher.objects.annotate(
        high_rated_books=Count('book', filter=Q(book__rating__gte=4))
    )
    return render(request, 'bookmodule/Task5.html', {'publishers': publishers})

def Task6(request):
    publishers = Publisher.objects.annotate(
        filtered_books=Count(
            'book',
            filter=Q(book__price__gt=50, book__quantity__lt=5, book__quantity__gte=1)
        )
    )
    return render(request, 'bookmodule/Task6.html', {'publishers': publishers})

def list_books_part1(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part1/listbooks.html', {'books': books})


def add_book_part1(request):
    if request.method == 'POST':
        book = Book.objects.create(
            title=request.POST.get('title'),
            price=request.POST.get('price'),
            quantity=request.POST.get('quantity'),
            pubdate=request.POST.get('pubdate'),
            rating=request.POST.get('rating'),
            publisher_id=request.POST.get('publisher')
        )

        book.authors.set(request.POST.getlist('authors'))

        return redirect('list_books_part1')

    publishers = Publisher.objects.all()
    authors = Author.objects.all()

    return render(request, 'bookmodule/lab9_part1/addbook.html', {
        'publishers': publishers,
        'authors': authors
    })


def edit_book_part1(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.price = request.POST.get('price')
        book.quantity = request.POST.get('quantity')
        book.pubdate = request.POST.get('pubdate')
        book.rating = request.POST.get('rating')
        book.publisher_id = request.POST.get('publisher')
        book.save()

        book.authors.set(request.POST.getlist('authors'))

        return redirect('list_books_part1')

    publishers = Publisher.objects.all()
    authors = Author.objects.all()

    return render(request, 'bookmodule/lab9_part1/editbook.html', {
        'book': book,
        'publishers': publishers,
        'authors': authors
    })


def delete_book_part1(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('list_books_part1')



def list_books_part2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab9_part2/listbooks.html', {'books': books})


def add_book_part2(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list_books_part2')

    else:
        form = BookForm()

    return render(request, 'bookmodule/lab9_part2/addbook.html', {'form': form})


def edit_book_part2(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('list_books_part2')

    else:
        form = BookForm(instance=book)

    return render(request, 'bookmodule/lab9_part2/editbook.html', {'form': form})


def delete_book_part2(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('list_books_part2')