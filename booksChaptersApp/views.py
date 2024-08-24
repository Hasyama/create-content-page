from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import *


def testing_view(request):
  books_DB_all = books_DB.objects.all()

  template = loader.get_template('debug_template.html')
  context = {
    'all_books': books_DB_all,
  }
  return HttpResponse(template.render(context, request))