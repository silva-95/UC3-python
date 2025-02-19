"""
URL configuration for exercicio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from principal import views as views_principal
from local import views as views_local
from sobre import views as views_sobre
from outros import views as views_outros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_principal.principal),
    path('principal/', views_principal.principal),
    path('local/', views_local.local),
    path('local/localizacao/', views_local.localizacao),
    path('sobre/', views_sobre.sobre),
    path('produtos/', views_sobre.produtos),
    path('servicos/', views_sobre.servicos),
    path('outros/', views_outros.outros),
]

