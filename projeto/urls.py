"""
URL configuration for projeto project.

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
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.conf import settings
from rest_framework import routers
from produto.views import TopicoViewSet

router = routers.DefaultRouter()
router.register('produto',TopicoViewSet)
# importaçao da biblioteca http
urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('unidade/', include('unidade.urls')),
    path('cadastro/', include('cadastro.urls')),
    path('comentario/', include('comentario.urls')),
    path('produto/', include('produto.urls')),
    path('carrinho/', include('carrinho.urls')),
]

#Adicione URLs de autenticação de site Django (para login, logout, gerenciamento de senha)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
