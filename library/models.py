from django.db import models
from datetime import *


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    date_of_birth = models.DateField(max_length=50)
    favorite_color = models.CharField(max_length=50, default='None')
    profile_picture = models.FileField(max_length=50, default='None')
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    validation_question = models.CharField(max_length=50)
    answer = models.CharField(max_length=50, default='None')
    comment = models.CharField(max_length=100, default='None')

    def __str__(self) -> str:
        return Customer.first_name, Customer.last_name


class Book(models.Model):
    name = models.CharField(max_length=20, default='None')
    author = models.CharField(max_length=20, default='None')
    publish_date = models.DateField('date published')
    book_type = models.CharField(max_length=20, default='1')

    def __str__(self) -> str:
        return Book.name


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField('The day the loan starts')
    return_date = models.DateField('Book return_date')

    def __str__(self) -> str:
        return Loan.book


# books_choices = ((1, "book1"), (2, "bbo2"))


# class Shop(models.Model):
#     book_name = models.CharField(books_choices, label="book"),
#     amount = models.CharField(label="amount"),

#     def __str__(self) -> str:
#         return Shop.book_name

books_choices = ((1, "book1"), (2, "bbo2"))


class Shop(models.Model):
    book_name = models.CharField(1),
    amount = models.CharField(),

    def __str__(self) -> str:
        return Shop.book_name