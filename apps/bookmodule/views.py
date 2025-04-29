from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.db.models import Q 
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Student, Address
from .models import Department, Course


def index(request): 
    name = request.GET.get("name") or "world!"  # Get the "name" parameter from URL
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1=0):  
    return HttpResponse("value1 = " + str(val1))

def viewbook(request, bookId): 
    # Assume these books are stored somewhere (e.g., a database)
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    
    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}  # Make book available in the template
    return render(request, 'bookmodule/show.html', context)

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links_page(request):
    return render(request, 'bookmodule/links.html')

def html5_links(request):
    return render(request, 'bookmodule/links.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html')


def html5_listing(request):
    return render(request, 'bookmodule/listing.html')

def html5_tables(request):
    return render(request, 'bookmodule/tables.html')

def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # Fetch the list of books
        books = getBooksList()
        newBooks = []

        # Filter the books based on the search criteria
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

def  getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'} 
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'} 
    return [book1, book2, book3]

def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')  # Checkbox returns 'on' or None
        isAuthor = request.POST.get('option2')

        books = getBooksList()
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

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects 
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request): 
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10] 
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks}) 
    else:
        return render(request, 'bookmodule/index.html')
    
def task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/task1.html', {'books': books})

def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=3) & ~Q(title__icontains='co') & ~Q(author__icontains='co')
    )
    return render(request, 'bookmodule/task3.html', {'books': books})

def task4(request):
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})



def task5(request):
    agg = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'agg': agg})


def task7(request):
    student_counts = Address.objects.annotate(num_students=Count('student'))
    return render(request, 'bookmodule/task7.html', {'student_counts': student_counts})


def lab9task1(request):
    departments = Department.objects.all()  
    department_counts = []
    for department in departments:
        count = department.student_set.count()  
        department_counts.append({'department': department, 'count': count})
    return render(request, 'bookmodule/lab9task1.html', {'department_counts': department_counts})

def lab9task2(request):
    courses = Course.objects.all()  
    course_counts = []
    for course in courses:
        count = course.student_set.count()  
        course_counts.append({'course': course, 'count': count})
    return render(request, 'bookmodule/lab9task2.html', {'course_counts': course_counts})


def lab9task3(request):
    departments = Department.objects.all() 
    oldest_students = []
    for department in departments:
        oldest_student = department.student_set.order_by('id').first() 
        oldest_students.append({'department': department, 'oldest_student': oldest_student})
    return render(request, 'bookmodule/lab9task3.html', {'oldest_students': oldest_students})

def lab9task4(request):
    departments = Department.objects.all()
    department_counts = []
    for department in departments:
        count = department.student_set.count()  
        if count > 2:  
            department_counts.append({'department': department, 'count': count})
    
    department_counts.sort(key=lambda x: x['count'], reverse=True)
    
    return render(request, 'bookmodule/lab9task4.html', {'department_counts': department_counts})




