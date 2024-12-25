from django.db import models
import re
from django.core.validators import ValidationError

# Fonction de validation  :Cette fonction vérifie si une chaîne de caractères ne contient que des lettres et des espaces.
def validate_title(value):
    if not re.match(r'^[A-Za-z\s]+$', value):
        raise ValidationError('This field should only contain letters and spaces.')

# Modèle Category : La classe Category que vous avez fournie est un modèle Django qui représente une catégorie dans votre application. Voici une explication détaillée de chaque partie de cette classe, ainsi qu'une suggestion pour la fonction de validation validate_title si elle n'a pas encore été définie :
class Category(models.Model):
    title = models.CharField(max_length=150, unique=True, validators=[validate_title])
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
#Cet attribut définit le nom pluriel du modèle lorsqu'il est affiché dans l'interface d'administration de Django.
    class Meta:
        verbose_name_plural = "categories"
#C'est une méthode magique (ou spéciale) en Python. Elle est appelée lorsque vous essayez de convertir une instance du modèle en chaîne de caractères (par exemple, lorsque vous imprimez l'objet ou l'affichez dans l'interface d'administration).
    def __str__(self):
        return self.title
    