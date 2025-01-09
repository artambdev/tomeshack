import uuid
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Ticket, TicketResponse
from .forms import TicketForm


def view_tickets(request):

    tickets = Ticket.objects.all()
    query = None

    if not request.user.is_superuser:
        tickets = Ticket.objects.filter(creator=request.user)

    context = {
        'tickets': tickets,
    }

    return render(request, 'support/tickets.html', context)


def create_ticket(request):
    """
    View function to handle rendering of ticket creation page
    and the submission of the ticket creation form
    """
    if request.method == "POST":
        ticket_form = TicketForm(data=request.POST)
        if ticket_form.is_valid():
            new_ticket = ticket_form.save(commit=False)
            new_ticket.uid = uuid.uuid4().hex.upper()
            new_ticket.creator = request.user
            new_ticket.resolved = False
            new_ticket.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your support ticket was successfully created'
            )
            return HttpResponseRedirect(
                reverse('view_ticket', args=[new_ticket.uid])
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'There was an error creating your ticket'
            )

    ticket_form = TicketForm()

    return render(
        request,
        "support/create_ticket.html",
        {
            "ticket_form": ticket_form,
        },
    )
