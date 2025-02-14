from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Ticket(models.Model):
    """
    Class to define the support ticket model
    """
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_tickets"
    )
    requester_email = models.EmailField(max_length=254)
    uid = models.SlugField(max_length=200, default=None, null=True)
    name = models.TextField(max_length=30)
    title = models.TextField(max_length=50)
    content = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField()

    def Meta(self):
        """
        Show the newest tickets first in admin screen
        """
        ordering = ["-created_on"]

    def __str__(self):
        return f'"{self.content[:15]}..." | requested by {self.name}'
    
    def get_resolved_str(self):
        """
        Returns a string describing if the ticket is resolved or not
        """
        if self.resolved:
            return 'Resolved'
        return 'Open'
    
    def get_num_responses_str(self):
        """
        Returns the number of ticket responses
        """
        num_responses = self.responses.count()
        response_or_responses = "responses"
        if num_responses == 1:
            response_or_responses = "response"
        return f'{num_responses} {response_or_responses}'


class TicketResponse(models.Model):
    """
    Class to define the support ticket response model
    """
    responder = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="ticket_responses"
    )
    uid = models.SlugField(max_length=200, default=None, null=True)
    response_to = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, related_name="responses"
    )
    content = models.TextField(max_length=400)
    posted_on = models.DateTimeField(auto_now_add=True)

    def Meta(self):
        """
        Show the newest responses first in admin screen
        """
        ordering = ["-posted_on"]

    def __str__(self):
        return f'"{self.content[:15]}..." | response made by {self.responder}'