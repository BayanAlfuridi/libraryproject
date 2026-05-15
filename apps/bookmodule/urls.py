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
    path('lab9/Task1', views.Task1),
    path('lab9/Task2', views.Task2),
    path('lab9/Task3', views.Task3),
    path('lab9/Task4', views.Task4),
    path('lab9/Task5', views.Task5),
    path('lab9/Task6', views.Task6),
    path('lab9_part1/listbooks', views.list_books_part1, name='list_books_part1'),
    path('lab9_part1/addbook', views.add_book_part1, name='add_book_part1'),
    path('lab9_part1/editbook/<int:id>', views.edit_book_part1, name='edit_book_part1'),
    path('lab9_part1/deletebook/<int:id>', views.delete_book_part1, name='delete_book_part1'),
    path('lab9_part2/listbooks', views.list_books_part2, name='list_books_part2'),
    path('lab9_part2/addbook', views.add_book_part2, name='add_book_part2'),
    path('lab9_part2/editbook/<int:id>', views.edit_book_part2, name='edit_book_part2'),
    path('lab9_part2/deletebook/<int:id>', views.delete_book_part2, name='delete_book_part2'),
    
    # Task 1
    path('bookmodule/lab11/students/', views.student_list, name='student_list'),
    path('bookmodule/lab11/students/add/', views.student_add, name='student_add'),
    path('bookmodule/lab11/students/update/<int:id>/', views.student_update, name='student_update'),
    path('bookmodule/lab11/students/delete/<int:id>/', views.student_delete, name='student_delete'),

    # Task 2
    path('bookmodule/lab11/students2/', views.student2_list, name='student2_list'),
    path('bookmodule/lab11/students2/add/', views.student2_add, name='student2_add'),
    path('bookmodule/lab11/students2/update/<int:id>/', views.student2_update, name='student2_update'),
    path('bookmodule/lab11/students2/delete/<int:id>/', views.student2_delete, name='student2_delete'),

    # Task 3
    path('bookmodule/lab11/clubs/', views.club_list, name='club_list'),
    path('bookmodule/lab11/clubs/add/', views.club_add, name='club_add'),


]



