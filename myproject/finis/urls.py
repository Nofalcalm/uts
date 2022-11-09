from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.awal,name='awal'),
    path('home',views.home,name='home'),
    path('kontak',views.kontak,name='kontak'),
    path('profil',views.profil,name='profil'),
]
