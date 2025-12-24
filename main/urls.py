from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('etudiants', views.EtudiantListView.as_view(), name='etudiant_list'),
    path('edtudiants/<int:pk>', views.EtudiantDetailView.as_view(), name='etudiant_detail'),
    path('inscriptions/', views.InscriptionListView.as_view(), name='inscription_list'),
    path('inscriptions/ajouter/', views.InscriptionCreateView.as_view(), name='inscription_add'),
    path('inscriptions/<int:pk>/modifier/', views.InscriptionUpdateView.as_view(), name='inscription_edit'),
    path('inscriptions/<int:pk>/supprimer/', views.InscriptionDeleteView.as_view(), name='inscription_delete'),
    path('filieres', views.FiliereListView.as_view(), name='filiere_list'),
]
