from django.db import models
from categoryApp.models import Category
from django.core.validators import MaxValueValidator,FileExtensionValidator
from django.core.validators import ValidationError
from datetime import date
import re
def validate_date(value):
    if value <= date.today():
        raise ValidationError('La date doit être dans le futur.')
def validate_cin(value):
    if not re.match(r'^\d{8}$', value):  
        raise ValidationError('The CIN should contain exactly 8 digits.')

        
# Create your models here.
class Conferance(models.Model):
    title=models.CharField( max_length=150)
    desciption=models.TextField( max_length=150)
    start_date=models.DateField( auto_now=False, auto_now_add=False,validators=[validate_date])
    #Cet argument détermine si le champ doit être automatiquement mis à jour avec la date et l'heure actuelles à chaque fois que l'objet est enregistré.
    end_date=models.DateField( auto_now=False, auto_now_add=False)
    location=models.CharField( max_length=50)
    price=models.FloatField()
    #controle de saisie
    capacity=models.IntegerField(validators=[MaxValueValidator(limit_value=1000,message="capacity cannot exceed 1000")])
    program=models.FileField( upload_to='files/',validators=[FileExtensionValidator(allowed_extensions=['pdf','png','jpeg','jpg'])])
    category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name='conferances')
    def clean (self):
     if self.end_date <= self.start_date:
          raise ValidationError("you can only resrve an upcoming conference")
        
        
    



    