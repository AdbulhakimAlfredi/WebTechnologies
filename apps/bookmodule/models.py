from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)

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
