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