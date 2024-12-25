from django import forms
from .models import Conferance
class conferanceModelForm(forms.ModelForm):
    class Meta:
        model=Conferance
        fields = '__all__'
    start_date=forms.DateField(
        label="conferance Start Date",
        widget=forms.DateInput(
            attrs={
                'type' : 'date',
                'class' :'form-control date-input'
            }
        ))
    end_date=forms.DateField(
        label="conferance End Date",
        widget=forms.DateInput(
            attrs={
                'type' : 'date',
                'class' :'form-control date-input'
            }
        ))