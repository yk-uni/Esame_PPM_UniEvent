from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.views.generic import ListView

from .models import Event
from .forms import EventForm
from .models import Event, Registration


class HomeView(ListView):

    model = Event

    template_name = 'events/home.html'

    context_object_name = 'events'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        registered_events = []

        if self.request.user.is_authenticated:

            registered_events = Registration.objects.filter(
                user=self.request.user
            ).values_list(
                'event_id',
                flat=True
            )

        context['registered_events'] = registered_events

        return context


@login_required
def create_event(request):

    if request.user.role != 'organizer':
        return HttpResponseForbidden(
            "Solo gli organizer possono creare eventi."
        )

    if request.method == 'POST':

        form = EventForm(request.POST)

        if form.is_valid():

            event = form.save(commit=False)

            event.organizer = request.user

            event.save()

            messages.success(request, "Evento creato con successo!")

            return redirect('home')

    else:

        form = EventForm()

    return render(
        request,
        'events/event_form.html',
        {'form': form}
    )

@login_required
def edit_event(request, pk):

    event = get_object_or_404(
        Event,
        pk=pk
    )

    if request.user.role != 'organizer':
        return HttpResponseForbidden(
            "Solo gli organizer possono modificare eventi."
        )


    if request.user != event.organizer:
        return HttpResponseForbidden(
            "Puoi modificare solo i tuoi eventi."
        )

    if request.method == 'POST':

        form = EventForm(
            request.POST,
            instance=event
        )

        if form.is_valid():

            form.save()

            messages.success(request, "Evento modificato con successo!")

            return redirect('home')

    else:

        form = EventForm(
            instance=event
        )

    return render(
        request,
        'events/event_form.html',
        {
            'form': form
        }
    )


@login_required
def delete_event(request, pk):

    event = get_object_or_404(
        Event,
        pk=pk
    )

    if request.user.role != 'organizer':
        return HttpResponseForbidden(
            "Solo gli organizer possono eliminare eventi."
        )

    if request.user != event.organizer:
        return HttpResponseForbidden(
            "Puoi eliminare solo i tuoi eventi."
        )

    if request.method == 'POST':

        event.delete()

        messages.success(request, "Evento eliminato con successo!")

        return redirect('home')

    return render(
        request,
        'events/delete_event.html',
        {
            'event': event
        }
    )


@login_required
def register_event(request, pk):

    if request.user.role != 'attendee':
        return HttpResponseForbidden(
            "Solo gli attendee possono iscriversi agli eventi."
        )

    event = get_object_or_404(Event, pk=pk)

    Registration.objects.get_or_create(
        user=request.user,
        event=event
    )

    messages.success(request, "Iscrizione completata!")

    return redirect('home')

@login_required
def dashboard(request):

    created_events = Event.objects.filter(
        organizer=request.user
    )

    registrations = Registration.objects.filter(
        user=request.user
    )

    return render(
        request,
        'events/dashboard.html',
        {
            'created_events': created_events,
            'registrations': registrations,
        }
    )