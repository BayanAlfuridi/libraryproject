from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.html5_links, name="books.html5_links"),
    path('html5/text/formatting/', views.html5_text_formatting, name="books.html5_text_formatting"),
    path('html5/listing/', views.html5_listing, name='html5_listing'),
    path('html5/tables/', views.tables_page, name='tables_page'),
    path('search/', views.search_books, name='search_books'),
    path('add/books', views.add_books),
    path('simple/query', views.simple_query),
    path('complex/query', views.complex_query),
    path('lab8/task1', views.task1),
    path('lab8/task2', views.task2),
    path('lab8/task3', views.task3),
    path('lab8/task4', views.task4),
    path('lab8/task5', views.task5),
    path('lab8/task7', views.task7),
]
