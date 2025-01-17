from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero

# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    """
    API endpoint to get all heroes
    """
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer