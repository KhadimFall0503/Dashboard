from django.contrib import admin
from .models import Etudiant, Filiere, Inscription

# Register your models here.
@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'date_naissance', 'telephone', 'date_creation')
    search_fields = ('nom', 'prenom', 'email')
    list_filter = ('date_creation',)
    ordering = ('nom', 'prenom')
    
@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    list_display = ('nom', 'code', 'duree')
    search_fields = ('nom', 'code')
    ordering = ('nom',)
    
@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'filiere', 'annee_academique', 'date_inscription')
    search_fields = ('etudiant__nom', 'etudiant__prenom', 'filiere__nom', 'annee_academique')
    list_filter = ('date_inscription', 'filiere')
    ordering = ('-date_inscription',)
