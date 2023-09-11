from django.shortcuts import render
from rest_framework import generics
from .models import Planet
from .serializers import PlanetSerializer

class PlanetView(generics.ListCreateAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
