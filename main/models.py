from django.db import models

# Create your models here.
class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
class Meta:
        ordering = ['nom', 'prenom']
        verbose_name = 'Étudiant'
        verbose_name_plural = 'Étudiants'
        
        
class Filiere(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    duree = models.IntegerField(help_text="Durée en années")

    def __str__(self):
        return self.nom
    
class Meta:
        ordering = ['nom']
        verbose_name = 'Filière'
        verbose_name_plural = 'Filières'
        
class Inscription(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    date_inscription = models.DateField(auto_now_add=True)
    annee_academique = models.CharField(max_length=9, help_text="Format: YYYY-YYYY")

    def __str__(self):
        return f"{self.etudiant} - {self.filiere} ({self.annee_academique})"