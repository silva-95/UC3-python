from django.urls import path
from . import views


urlpatterns = [
    path('', views.outros),
    path('outros/', views.outros),
    path('atividade/', views.atividade),
]