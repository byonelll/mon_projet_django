from django import forms
from .models import Member  # On importe le modèle pour lequel on crée le formulaire
from .models import Contribution
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone']  # Champs que l'on veut dans le formulaire

class ContributionForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = ['member', 'amount', 'description']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # Ajoute d'autres champs si nécessaire

