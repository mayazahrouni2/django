from django.db import models
from django.contrib.auth.models import AbstractUser
from conferanceApp.models import Conferance
import re
from django.core.validators import ValidationError,RegexValidator
from django.utils import timezone


def validate_cin(value):
    if not re.match(r'^\d{8}$', value):  
        raise ValidationError('The CIN should contain exactly 8 digits.')

# Create your models here.
class Participant(AbstractUser):
#  cin_validator=RegexValidator(
#  regex=r'^\d{8}$',
# message='The CIN should contain exactly 8 digits.'
#     )
 email_validator = RegexValidator(
    regex=r'^[\w\.-]+@esprit\.tn$',  
    message='Email must end with @esprit.tn'
 )
#  def validate_email(value):
#      if not  value.endwith("@esprit.tn"):
#          raise ValidationError('Email must end with @esprit.tn')
 cin=models.CharField(max_length=8, primary_key=True,validators=[validate_cin])
 email=models.EmailField(max_length=254, unique=True,validators=[email_validator])
 username=models.CharField(max_length=20, unique=True)
 USERNAME_FIELD="username"
 choix=(("Etudiant","Etudiant"),("Enseignant","Enseignant"),("Doctorant","Doctorant"),("Chercheur","Chercheur"))
 participant_category=models.CharField(max_length=50,choices=choix)
 reservations= models.ManyToManyField(Conferance,through='Reservation',related_name='reservations')
 
class Reservation(models.Model):
 participant=models.ForeignKey(Participant,on_delete=models.CASCADE)
 conferance=models.ForeignKey(Conferance, on_delete=models.CASCADE)
 reservation_date = models.DateField(default=timezone.now)
 confirmed=models.BooleanField(default=False)
 def clean (self):
     if self.reservation_date > self.conferance.start_date:
         raise ValidationError("End date must be set begin start date")
     today = timezone.now().date()
        
     reservations_today = Reservation.objects.filter(
            participant=self.participant,
            reservation_date=today
        ).count()
        
     if reservations_today >= 3:
            raise ValidationError('You cannot make more than 3 reservations day.')

 def __str__(self):
        return f'Reservation by {self.participant.username} for {self.conferance.title}'
     
    
