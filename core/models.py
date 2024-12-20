from django.db import models


class Member(models.Model):
    """
    Modèle représentant un membre de l'association.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    """
    Modèle représentant un événement organisé par l'association.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Contribution(models.Model):
    """
    Modèle représentant une cotisation associée à un membre.
    """
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='contributions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.member.name} - {self.amount}€ le {self.date}"

from django.db import models
from django.contrib.auth.models import User

class JobOffer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    published_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    source_url = models.URLField(max_length=500, null=True, blank=True)  # Lien externe pour l'offre

    def __str__(self):
        return self.title




class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(
        max_length=50,
        choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')],
        default='Pending'
    )
    applied_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.job_offer.title} ({self.status})"

class Job(models.Model):

    title = models.CharField(max_length=200)  # Titre de l'offre d'emploi
    description = models.TextField()  # Description détaillée
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création

    def __str__(self):
        return self.title

