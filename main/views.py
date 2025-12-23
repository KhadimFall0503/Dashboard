from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

# Import des modèles
from .models import Etudiant, Filiere, Inscription

# -----------------------
# DASHBOARD
# -----------------------

class DashboardView(TemplateView):
    template_name = "main/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.request.GET.get('q', '')
        etudiants = Etudiant.objects.all()
        if q:
            etudiants = etudiants.filter(nom__icontains=q) | etudiants.filter(prenom__icontains=q)
        context["etudiants"] = etudiants
        context["filieres"] = Filiere.objects.all()
        context["inscriptions"] = Inscription.objects.all()
        context["nb_etudiants"] = Etudiant.objects.count()
        context["nb_filieres"] = Filiere.objects.count()
        context["nb_inscriptions"] = Inscription.objects.count()
        return context
# -----------------------
# ÉTUDIANTS
# -----------------------
class EtudiantListView(ListView):
    model = Etudiant
    template_name = "students/etudiant_list.html"
    context_object_name = "etudiants"
    paginate_by = 10
    
class EtudiantDetailView(DetailView):
    model = Etudiant
    template_name = "main/etudiant_detail.html"
    context_object_name = "etudiant"

class EtudiantCreateView(CreateView):
    model = Etudiant
    fields = ["nom", "prenom", "date_naissance", "email", "telephone"]
    template_name = "students/etudiant_form.html"
    success_url = reverse_lazy("etudiant_list")

class EtudiantUpdateView(UpdateView):
    model = Etudiant
    fields = ["nom", "prenom", "date_naissance", "email", "telephone"]
    template_name = "students/etudiant_form.html"
    success_url = reverse_lazy("etudiant_list")

class EtudiantDeleteView(DeleteView):
    model = Etudiant
    template_name = "students/etudiant_confirm_delete.html"
    success_url = reverse_lazy("etudiant_list")

# -----------------------
# FILIÈRES
# -----------------------
class FiliereListView(ListView):
    model = Filiere
    template_name = "main/filiere_list.html"
    context_object_name = "filieres"

# -----------------------
# INSCRIPTIONS
# -----------------------
class InscriptionListView(ListView):
    model = Inscription
    template_name = "inscriptions/inscription_list.html"
    context_object_name = "inscriptions"
