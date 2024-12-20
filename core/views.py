from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from .forms import MemberForm, ContributionForm
from .models import Member, Event, Contribution, JobOffer, Application
from .serializers import (EventSerializer, MemberSerializer, ContributionSerializer,
                          JobOfferSerializer, ApplicationSerializer)


# --- Vues pour l'accueil et l'API ---
def home(request):
    """
    Vue pour la page d'accueil.
    """
    return render(request, 'core/index.html')


@api_view(['GET'])
def api_home(request):
    """
    Vue API de base.
    """
    return Response({"message": "Bienvenue dans l'API de l'association"})


# --- Gestion des membres ---
class MemberViewSet(ModelViewSet):
    """
    ViewSet pour gérer les membres.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


# --- Gestion des événements ---
class EventViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour gérer les événements.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


def event_list(request):
    """
    Liste tous les événements.
    """
    events = Event.objects.all()
    return render(request, 'core/event_list.html', {'events': events})


def event_detail(request, pk):
    """
    Affiche le détail d'un événement.
    """
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'core/event_detail.html', {'event': event})


def event_create(request):
    """
    Crée un nouvel événement.
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        Event.objects.create(
            title=title, description=description, date=date, time=time, location=location
        )
        return redirect('event_list')
    return render(request, 'core/event_form.html')


def event_delete(request, pk):
    """
    Supprime un événement.
    """
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('event_list')


# --- Gestion des cotisations ---
class ContributionViewSet(ModelViewSet):
    """
    ViewSet pour gérer les cotisations (CRUD via API).
    """
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer


def contribution_list_view(request):
    """
    Affiche la liste des cotisations via un template HTML.
    """
    contributions = Contribution.objects.all()
    return render(request, 'core/contribution_list.html', {'contributions': contributions})


@api_view(['GET'])
def contribution_list(request):
    """
    Liste des cotisations au format JSON via API.
    """
    contributions = Contribution.objects.all()
    serializer = ContributionSerializer(contributions, many=True)
    return Response(serializer.data)

# Liste des cotisations
def contribution_list(request):
    contributions = Contribution.objects.all().order_by('-date')
    return render(request, 'core/contribution_list.html', {'contributions': contributions})

# --- Gestion des offres d'emploi ---
class JobOfferViewSet(ModelViewSet):
    """
    ViewSet pour gérer les offres d'emploi via API.
    """
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer


class ApplicationViewSet(ModelViewSet):
    """
    ViewSet pour gérer les candidatures via API.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


def job_offer_list(request):
    """
    Affiche la liste des offres d'emploi via un template HTML.
    """
    job_offers = JobOffer.objects.all()  # Récupère toutes les offres
    return render(request, 'core/job_offer_list.html', {'job_offers': job_offers})


def application_list(request):
    """
    Affiche la liste des candidatures via un template HTML.
    """
    applications = Application.objects.all()  # Récupère toutes les candidatures
    return render(request, 'core/application_list.html', {'applications': applications})

def member_list(request):
    members = Member.objects.all()
    return render(request, 'core/member_list.html', {'members': members})

def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'core/member_detail.html', {'member': member})

def member_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Member.objects.create(name=name, email=email, phone=phone)
        return redirect('member_list')
    return render(request, 'core/member_form.html')

def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.delete()
    return redirect('member_list')

def member_edit(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')  # Redirige vers la liste des membres après la mise à jour
    else:
        form = MemberForm(instance=member)
    return render(request, 'core/member_edit.html', {'form': form})

# Ajouter une cotisation
def contribution_add(request):
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contribution_list')
    else:
        form = ContributionForm()
    return render(request, 'core/contribution_form.html', {'form': form})

# Modifier une cotisation
def contribution_edit(request, pk):
    contribution = get_object_or_404(Contribution, pk=pk)
    if request.method == 'POST':
        form = ContributionForm(request.POST, instance=contribution)
        if form.is_valid():
            form.save()
            return redirect('contribution_list')
    else:
        form = ContributionForm(instance=contribution)
    return render(request, 'core/contribution_form.html', {'form': form})

# Supprimer une cotisation
def contribution_delete(request, pk):
    contribution = get_object_or_404(Contribution, pk=pk)
    if request.method == 'POST':
        contribution.delete()
        return redirect('contribution_list')
    return render(request, 'core/contribution_confirm_delete.html', {'contribution': contribution})


def joboffer_detail(request, offer_id):  # Doit correspondre au nom défini dans l'URL
    job_offer = get_object_or_404(JobOffer, id=offer_id)
    return render(request, 'joboffer_detail.html', {'job_offer': job_offer})


def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été créé avec succès ! Vous pouvez maintenant vous connecter.')
            return redirect('dashboard')  # Redirige vers la page du tableau de bord
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

def connexion(request):
    return render(request, 'login.html')

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirige vers le tableau de bord
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': form})

@login_required
def update_profile(request):
    # Logique pour la mise à jour du profil
    return render(request, 'core/update_profile.html')



