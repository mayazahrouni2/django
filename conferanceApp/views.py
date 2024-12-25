from django.shortcuts import render
from conferanceApp.models import Conferance
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy #reverse_lazy, qui est utilisé pour créer des URL de manière paresseuse (c'est-à-dire qu'elle ne sera évaluée que lorsque cela sera nécessaire).
from .forms import conferanceModelForm
from participantApp.models import Reservation

# def conferenceList(request):
#     list=Conferance.objects.all()
#     return render(request,'conferance\conferance_list.html',{
#         'list' : list    })

# qui est utilisée pour afficher une liste de conférences
class ConferenceListView(ListView):
    model = Conferance
    template_name='conferanceApp/conference.html'
    context_object_name = "list"
# qui est utilisée pour afficher les détails de conférences

class conferenceDetailView(DetailView):
    model = Conferance
    template_name='conferanceApp/conference_detail.html'
    context_object_name = "conference"
    
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      Conferance = self.get_object()
    # Récupérer les réservations associées à cette conférence
      context['reservations'] = Reservation.objects.filter(conferance=Conferance)
      return context
  #Cette méthode permet d'ajouter des données supplémentaires au contexte qui sera passé au template.
# super().get_context_data(**kwargs) : Cela appelle la méthode parente pour obtenir le contexte de base.
# conference = self.get_object() : Cela récupère l'objet Conference spécifique que vous souhaitez afficher (l'instance que vous avez sélectionnée).
# context['reservations'] = Reservation.objects.filter(conference=conference) : Cela récupère toutes les réservations associées à cette conférence en utilisant une requête filtrée et les ajoute au contexte sous la clé 'reservations'.
# return context : Cela retourne le contexte mis à jour, qui inclut maintenant les réservations associées à la conférence.

class conferenceCreateView(CreateView):
    model = Conferance
    template_name='conferanceApp/conference_form.html'
    #fields=['title','desciption','start_date','end_date','location','price','capacity','program','category']
    success_url=reverse_lazy('conferance_list')
    #Cet attribut définit l'URL vers laquelle l'utilisateur sera redirigé après une création réussie de la conférence.
    form_class=conferanceModelForm
    #Cet attribut spécifie le formulaire à utiliser pour la création de l'objet.

class conferenceUpdateView(UpdateView):
    model = Conferance
    template_name='conferanceApp/conference_form.html'
    success_url=reverse_lazy('conferance_list')
    form_class=conferanceModelForm

class conferenceDeleteView(DeleteView):
    model = Conferance
    template_name='conferanceApp/conference_delete.html'
    success_url=reverse_lazy('conferance_list')