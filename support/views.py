import uuid
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Ticket, TicketResponse
from .forms import TicketForm, TicketResponseForm


def view_tickets(request):
    tickets = Ticket.objects.all()
    query = None

    if not request.user.is_superuser:
        tickets = Ticket.objects.filter(creator=request.user)

    context = {
        'tickets': tickets,
    }

    return render(request, 'support/tickets.html', context)


def view_ticket(request, uid):
    """
    View function to render ticket's individual pages
    """
    ticket = get_object_or_404(Ticket.objects.all(), uid=uid)

    queryset = ticket.responses
    responses = queryset.order_by("posted_on")
    num_responses = queryset.count()

    if request.method == "POST":
        response_form = TicketResponseForm(data=request.POST)
        if response_form.is_valid():
            response_form = response_form.save(commit=False)
            response_form.uid = uuid.uuid4().hex.upper()
            response_form.response_to = ticket
            response_form.responder = request.user
            response_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Response created successfully'
            )
            return HttpResponseRedirect(
                reverse('view_ticket', args=[ticket.uid])
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'There was an error creating a response to this ticket'
            )

    ticket_response_form = TicketResponseForm()

    return render(
        request,
        "support/view_ticket.html",
        {
            "ticket": ticket,
            "responses": responses,
            "num_responses": num_responses,
            "response_form": ticket_response_form,
        },
    )


def resolve_ticket(request, uid):
    """
    View function to handle ticket resolve requests
    """
    queryset = Ticket.objects.all()
    ticket = get_object_or_404(queryset, uid=uid)

    if request.user.is_superuser:
        ticket.resolved = not ticket.resolved
        ticket.save()
        message_string = "Ticket is now resolved"
        if not ticket.resolved:
            message_string = "Ticket is now open"
        messages.add_message(
            request, messages.SUCCESS,
            message_string
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'There was an error in setting the resolved status of this ticket'
        )

    return HttpResponseRedirect(reverse('view_ticket', args=[ticket.uid]))


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
