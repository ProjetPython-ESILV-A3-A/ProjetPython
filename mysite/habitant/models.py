from django.db import models

# Create your models here.

class Produit(models.Model):
    nomProduit=models.CharField(max_length=40)
    quantitemax=models.IntegerField()
    prix=models.IntegerField()
    def __str__(self):
        return nomProduit
    def allstr(self):
        return nomProduit + " "+quantitemax+" /personnes, prix : " +prix
