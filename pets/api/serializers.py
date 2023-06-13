from rest_framework import serializers
from .models import AnimalClass, Breed


class AnimalClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalClass
        fields = ['name', 'description']


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = [
            'name', 'animal_class',
            'description', 'origin',
            'average_weight', 'lifespan',
            'lifespan_unit', 'temperament'
        ]
