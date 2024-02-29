# Ex02 Django ORM Web Application
## Date: 29.02.2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![alt text](<nei/nei/Entity diagram.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
models.py

from django.db import models
from django.contrib import admin 
class Book(models.Model):
    Bookid=models.IntegerField(primary_key=True);
    Bookname=models.CharField(max_length=20);
    Bookauthor=models.CharField(max_length=50);
    Bookprice=models.IntegerField();
    Bookgenre=models.CharField(max_length=20);
class BookAdmin(admin.ModelAdmin):
    list_display=("Bookid","Bookname","Bookauthor","Bookprice","Bookgenre");


admin.py

from django.contrib import admin
from .models import Book,BookAdmin
admin.site.register(Book,BookAdmin)
```
## OUTPUT

![alt text](<nei/nei/Website Book link.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
