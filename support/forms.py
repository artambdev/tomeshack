from django import forms
from .models import Ticket, TicketResponse


class TicketForm(forms.ModelForm):
    """
    Form for creating a support ticket to get admin attention
    """
    class Meta:
        model = Ticket
        fields = ('requester_email', 'name', 'title', 'content')


class TicketResponseForm(forms.ModelForm):
    """
    Form for creating a support ticket to get admin attention
    """
    class Meta:
        model = TicketResponse
        fields = ('content')