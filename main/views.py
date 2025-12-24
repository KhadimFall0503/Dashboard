from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)
from django.urls import reverse_lazy
from django.db.models import Q

# Import des modèles
from .models import Etudiant, Filiere, Inscription


# =====================================================
# DASHBOARD
# =====================================================
class DashboardView(TemplateView):
    template_name = "main/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        q = self.request.GET.get("q", "")

        # Derniers 10 étudiants
        etudiants = Etudiant.objects.all().order_by('-id')
        if q:
            etudiants = etudiants.filter(Q(nom__icontains=q) | Q(prenom__icontains=q))
        context["etudiants"] = etudiants[:10]

        # Dernières 10 inscriptions
        inscriptions = Inscription.objects.select_related('etudiant', 'filiere').order_by('-date_inscription')
        context["inscriptions"] = inscriptions[:5]

        # Dernières 10 filières
        filieres = Filiere.objects.all().order_by('-id')
        context["filieres"] = filieres[:5]

        # Statistiques
        context["nb_etudiants"] = Etudiant.objects.count()
        context["nb_filieres"] = Filiere.objects.count()
        context["nb_inscriptions"] = Inscription.objects.count()

        return context

class AboutView(TemplateView):
    template_name = "main/about.html"

# =====================================================
# ÉTUDIANTS
# =====================================================
class EtudiantListView(ListView):
    model = Etudiant
    template_name = "students/etudiant_list.html"
    context_object_name = "etudiants"
    paginate_by = 10


class EtudiantDetailView(DetailView):
    model = Etudiant
    template_name = "main/etudiant_detail.html"
    context_object_name = "etudiant"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["inscriptions"] = Inscription.objects.filter(
            etudiant=self.object
        ).select_related("filiere")
        return context


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


# =====================================================
# FILIÈRES
# =====================================================
class FiliereListView(ListView):
    model = Filiere
    template_name = "main/filiere_list.html"
    context_object_name = "filieres"

    def get_queryset(self):
        q = self.request.GET.get("q", "")
        queryset = Filiere.objects.all()
        if q:
            queryset = queryset.filter(Q(nom__icontains=q) | Q(code__icontains=q))
        return queryset


class FiliereCreateView(CreateView):
    model = Filiere
    fields = ["nom", "code", "duree", "description"]
    template_name = "main/filiere_form.html"
    success_url = reverse_lazy("filiere_list")


class FiliereUpdateView(UpdateView):
    model = Filiere
    fields = ["nom", "code", "duree", "description"]
    template_name = "main/filiere_form.html"
    success_url = reverse_lazy("filiere_list")


class FiliereDeleteView(DeleteView):
    model = Filiere
    template_name = "main/filiere_confirm_delete.html"
    success_url = reverse_lazy("filiere_list")


# =====================================================
# INSCRIPTIONS
# =====================================================
class InscriptionListView(ListView):
    model = Inscription
    template_name = "main/inscription_list.html"
    context_object_name = "inscriptions"
    paginate_by = 10

    def get_queryset(self):
        return Inscription.objects.select_related("etudiant", "filiere").order_by("-date_inscription")


class InscriptionCreateView(CreateView):
    model = Inscription
    fields = ["etudiant", "filiere", "annee_academique"]
    template_name = "main/inscription_form.html"
    success_url = reverse_lazy("inscription_list")


class InscriptionUpdateView(UpdateView):
    model = Inscription
    fields = ["etudiant", "filiere", "annee_academique"]
    template_name = "main/inscription_form.html"
    success_url = reverse_lazy("inscription_list")


class InscriptionDeleteView(DeleteView):
    model = Inscription
    template_name = "main/inscription_confirm_delete.html"
    success_url = reverse_lazy("inscription_list")


# =====================================================
# INSCRIPTION DEPUIS UN ÉTUDIANT
# =====================================================
class InscriptionCreateForEtudiantView(CreateView):
    model = Inscription
    fields = ["filiere", "annee_academique"]
    template_name = "main/inscription_form.html"  # Utilise le même template

    def form_valid(self, form):
        form.instance.etudiant = Etudiant.objects.get(pk=self.kwargs["etudiant_id"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("etudiant_detail", kwargs={"pk": self.kwargs["etudiant_id"]})
