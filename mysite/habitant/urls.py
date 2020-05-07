"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from . import views 

urlpatterns = [
    path('connexion/',views.ConnexionUser, name='connexion'),
    path('inscription/',views.InscriptionUser, name='inscription'),
    path('demande/',views.DemandeUser, name='demande'),
    path('special/',views.SpecialUser, name='special'),
    path('panier/',views.PanierUser, name='panier'),
    path('paiement/',views.PaiementUser, name='paiement'),
]
