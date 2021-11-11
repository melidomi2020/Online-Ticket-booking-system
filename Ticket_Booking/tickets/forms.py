from django import  forms
#from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from django.forms import fields
from .models import Ticket


class ticketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields=('user','counter','service')