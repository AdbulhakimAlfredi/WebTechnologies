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


class Department(models.Model):
    name = models.CharField(max_length=100)

class Card(models.Model):
    card_number = models.IntegerField()

class student2(models.Model):
    name = models.CharField(max_length=100)
    Card_number = models.OneToOneField( Card, 
    on_delete=models.PROTECT, 
    related_name='student2' 
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='students'
    )





    

