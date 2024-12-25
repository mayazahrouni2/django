from django.contrib import admin
from .models import Conferance
from participantApp.models import Reservation

#lors de la créeation  d'une conférence tu peux reserver 
#Cela définit une classe d'interface d'administration qui permet d'ajouter des réservations directement dans la page de création ou de modification d'une conférence
class ReservationInline(admin.StackedInline):
    model= Reservation
    #Cela signifie qu'un formulaire vide pour une réservation sera affiché par défaut. Vous pouvez ajouter plus d'instances de réservation.
    extra = 1
    #Cela permet à l'utilisateur de supprimer des réservations existantes.
    can_delete = True
    #est en lecture seule dans l'interface d'administration. L'utilisateur ne pourra pas le modifier.
    readonly_fields=('reservation_date',) 
    


class ConferanceAdmin(admin.ModelAdmin):
    # spécifie les champs qui seront affichés dans la liste des objets Conferance dans l'interface d'administration.
    list_display=('title','start_date','end_date')
    #l'ordre dans lequel les conférences seront affichées dans la liste.
    ordering=('title','start_date')
    #list_per_page=1  elle limiterait le nombre de conférences affichées par page à 1
    #readonly_fields=('created_at','updated_at')
    #Cela ajoute un filtre à la barre latérale de l'interface d'administration. Les administrateurs peuvent filtrer les conférences par titre.
    list_filter=('title',)
    # permet d'ajouter une barre de recherche dans l'interface d'administration. Les utilisateurs peuvent rechercher des conférences par titre ou emplacement.
    search_fields=('title','location',)
    #d'utiliser l'autocomplétion pour le champ category (catégorie) dans le formulaire de création et de modification d'une conférence.
    autocomplete_filds=('category',)
    #d'afficher les réservations associées à chaque conférence dans un formulaire imbriqué (inline) lors de la création ou de la modification d'une conférence. ReservationInline
    inlines=[ReservationInline]

#pour connaitre le model
admin.site.register(Conferance,ConferanceAdmin)


    