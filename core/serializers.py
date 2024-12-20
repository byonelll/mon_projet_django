from rest_framework import serializers
from .models import Event, Member, Contribution, JobOffer, Application

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = '__all__'


class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
