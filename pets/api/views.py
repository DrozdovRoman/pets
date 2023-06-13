from django.shortcuts import render
from rest_framework import viewsets
from .models import Breed, AnimalClass
from .serializers import BreedSerializer, AnimalClassSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class AnimalClassViewSet(viewsets.ModelViewSet):
    queryset = AnimalClass.objects.all()
    serializer_class = AnimalClassSerializer
