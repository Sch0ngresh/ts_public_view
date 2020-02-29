"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm
from app.models import Ticket
from app.models import Tech_update
from django.contrib.auth.models import User
from django.forms import BaseModelFormSet

from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class Ticket_form(forms.ModelForm):
    class Meta:
        model = Ticket
        labels = {
            'custID':'Location:',
            'ticketID':'Problem:',
            'description':'Description:',
            'room_num':'Room:',
            'severity':'Urgency:',
            'aff_work':'Affecting Work?:',
            'aff_num':'Number Affected:',
            'contact_method':'Contact Method:',

            }
        fields = ['custID','ticketID','description','room_num','contact','contact_method','severity','aff_work','aff_num','document']

class DateInput(forms.DateInput):
    input_type = 'date'

class Ticket_update(forms.ModelForm):
    class Meta:
        model = Ticket
        labels = {
            "ticket_completed":"Ticket Updated:",
            }
        widgets = {
            'ticket_completed': DateInput()
            }
        fields = ['ticket_completed','ticket_fix','status']
    
class TechUpdate(forms.ModelForm):
    class Meta:
        model = Tech_update
        labels = {
            "tech_date":"Ticket Date:",
            }
        widgets = {
            'tech_date': DateInput()
            }
        fields = ['tech_date','tech_notes','tech_status']