from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
   path('',views.home,name='home'),
   path('contact/', views.contacts, name='contact'), 
   path('services/', views.services, name='services'),
   path('about/', views.about, name='about'),
   path('Reikihealing/', views.Reikihealing, name='Reikihealing'),
   path('tarotcardreading/', views.tarotcardreading, name='tarotcardreading'),
   path('lamaferahealing/', views.lamaferahealing, name='lamaferahealing'),
   path('admin/', admin.site.urls),
   path('pendulumdowsing/', views.pendulumdowsing, name='pendulumdowsing'),
   path('certifications/', views.certifications, name='certifications'),

]
