from django import forms
from .models import Ticket, TicketResponse


class TicketForm(forms.ModelForm):
    """
    Form for creating a support ticket to get admin attention
    """
    class Meta:
        model = Ticket
        fields = ('requester_email', 'name', 'title', 'content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['requester_email'].label = "Your email:"
        self.fields['name'].label = "Your name:"
        self.fields['title'].label = "Issue you're having:"
        self.fields['content'].label = "Details:"


class TicketResponseForm(forms.ModelForm):
    """
    Form for creating a support ticket to get admin attention
    """
    class Meta:
        model = TicketResponse
        fields = ('content',)