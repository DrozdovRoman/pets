from django.contrib import admin
from .models import AnimalClass, Breed


@admin.register(AnimalClass)
class AnimalClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Breed)
class Breed(admin.ModelAdmin):
    list_display = ('name', 'animal_class',)
    list_display_links = ('name',)
    search_fields = ('name',)

