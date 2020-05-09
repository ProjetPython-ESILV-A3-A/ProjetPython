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
from django.urls import path
from . import views

urlpatterns = [
    path('',views.communeBase,name="base"),
    path('action/',views.communeaction,name="action"),
    path('produits/',views.communeproduitChoix,name="produits"),
    path('produits/add/',views.communeproduitAdd,name="ajoutProd"),
    path('produits/sub/',views.communeproduitSub,name="retireProd"),
    path('produits/sub/validation/<Produitasupprimer>/',views.communevalidsuppr,name="retireProd"),
    path('Visualisation/',views.communevisuchoix,name="visuchoix"),
    path('Visualisation/<int:numeroVu>/',views.communeVisualisation,name="visu"),
]
