from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('<int:bookId>/', views.viewbook, name="books.viewbook"),
    path('html5/links', views.html5_links, name='html5_links'),
    path('html5/listing', views.html5_listing, name='html5_listing'),
    path('html5/tables', views.html5_tables, name='html5_tables'),
    path('html5/formatting/', views.formatting, name='formatting'),
    path('search/', views.search_books, name='books_search'), 
    path('simple/query/', views.simple_query, name='simple_query'),
    path('complex/query/', views.complex_query, name='complex_query'),
    path('lab8/task1/', views.task1, name='task1'),
    path('lab8/task2/', views.task2, name='task2'),
    path('lab8/task3/', views.task3, name='task3'),
    path('lab8/task4/', views.task4, name='task4'),
    path('lab8/task5/', views.task5, name='task5'),
    path('lab8/task7/', views.task7, name='task7'),
    path('lab9/task1/', views.lab9task1, name='Lab9Task1'),
    path('lab9/task2/', views.lab9task2, name='Lab9Task2'),
    path('lab9/task3/', views.lab9task3, name='Lab9Task3'),
    path('lab9/task4/', views.lab9task4, name='Lab9Task4'),
    
    path('lab10_part1/listbooks', views.list_booksP1, name='list_booksP1'),
    path('lab10_part1/addbook', views.add_bookP1, name='add_bookP1'),
    path('lab10_part1/editbook/', views.edit_bookP1, name='edit_bookP1'),
    path('lab10_part1/deletebook/', views.delete_bookP1, name='delete_bookP1'),

    path('lab10_part2/listbooks', views.list_booksP2, name='list_booksP2'),
    path('lab10_part2/addbook/', views.add_bookP2, name='add_bookP2'),
    path('lab10_part2/editbook/', views.edit_bookP2, name='edit_bookP2'),
    path('lab10_part2/deletebook/', views.delete_bookP2, name='delete_bookP2'),
    path('students/', views.student_list, name='student_list'),
    path('student/add/', views.student_add, name='student_add'),
    path('student/<int:pk>/image/', views.student_image_upload, name='student_image_upload'),
] 