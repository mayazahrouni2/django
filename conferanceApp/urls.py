from django.urls import path
from .views import *

urlpatterns=[
    path('list/',ConferenceListView.as_view(),name='conferance_list'),
    #path('list/',conferenceList,name='conferance_list') (ki namel ena le fichier html)
    path('details/<int:pk>',conferenceDetailView.as_view(),name='conferance_detail'),
    path('create',conferenceCreateView.as_view(),name='conferance_create'),
    path('update/<int:pk>',conferenceUpdateView.as_view(),name='conferance_update'),
    path('delete/<int:pk>',conferenceDeleteView.as_view(),name='conferance_delete')
]