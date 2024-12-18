from django.urls import path
from . import views


urlpatterns = [
    path('', views.local),
    path('localizacao/', views.localizacao),
    path('local/', views.local),
]