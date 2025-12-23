from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('etudiants', views.EtudiantListView.as_view(), name='etudiant_list'),
    path('edtudiants/<int:pk>', views.EtudiantDetailView.as_view(), name='etudiant_detail'),
    path('filieres', views.FiliereListView.as_view(), name='filiere_list'),
]
