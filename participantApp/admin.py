from django.contrib import admin
from participantApp.models import Participant,Reservation


class ParticipantAdmin(admin.ModelAdmin):
    pass
admin.site.register(Participant,ParticipantAdmin)
class ReservationAdmin(admin.ModelAdmin):
    #action
    list_display=('conferance','participant','confirmed',)
    actions= ['confirm_action',]
    def confirm_action(self,request,queryset):
        queryset.update(confirmed=True)
        self.messade_user(request,"selected reservations have been confirmed")
    confirm_action.short_description = "confirm reservations"
    
    
    
admin.site.register(Reservation,ReservationAdmin)