# myApp/models.py
from django.db import models


# Create your models here.
# books table #
class books_DB(models.Model):
  #pk is book_id
  book_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
  book_name = models.CharField(max_length=100)

# chapters table #
class chapters_DB(models.Model):
  #pk is chapter_id
  chapter_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
  #foreign key 'book_id' from 'books_DB' 
  book_id = models.ForeignKey(books_DB, on_delete=models.CASCADE, default=None)
  chapter_name = models.CharField(max_length=100)