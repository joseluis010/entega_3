
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('crear-autor/', views.crear_autor, name="crear_autor" ),

]
