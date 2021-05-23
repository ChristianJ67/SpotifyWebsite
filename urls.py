from django.urls import path

from . import views

urlpatterns = [
    path('secondpage/', views.secondpage, name='secondpage'),
    path('homepage/', views.homepage, name='homepage'),
    path('', views.index, name='index'),
]
