
from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.testing_view),
]
