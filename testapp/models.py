from django.db import models
class Vehicule (models.Model): 
    matricule=models.CharField((""), max_length=10,primary_key=True)
    modele=models.CharField((""), max_length=20)
    prix=models.DecimalField(("price"), max_digits=5, decimal_places=2)
    description=models.TextField((""), blank=True)
