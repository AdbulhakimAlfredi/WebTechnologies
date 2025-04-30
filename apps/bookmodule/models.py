from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    edition = models.CharField(max_length=100)
    isbn_number = models.CharField(max_length=13, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)

class Address(models.Model):
    city = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()

class Card(models.Model):
    card_number = models.IntegerField()

class Department(models.Model):
    name = models.CharField(max_length=100)

class Student2(models.Model):  
    name = models.CharField(max_length=100)
    card = models.OneToOneField(Card, on_delete=models.PROTECT, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
