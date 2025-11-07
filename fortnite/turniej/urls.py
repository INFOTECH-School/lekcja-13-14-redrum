from django.urls import path
from . import views

urlpatterns = [
    path('zapis/', views.zapisz_sie, name='zapisz_sie'),
    path('turnieje/', views.lista_turniejow, name='lista_turniejow'),
    path('profile/', views.profile_view, name='profile'),

]
