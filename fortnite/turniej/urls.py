from django.urls import path
from . import views

urlpatterns = [
    path('zapis/', views.zapisz_sie, name='zapis'),
]
