from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core import views

# Configuration du routeur pour les API
router = DefaultRouter()
router.register('members', views.MemberViewSet, basename='members')
router.register('events', views.EventViewSet, basename='event')
router.register('contributions', views.ContributionViewSet, basename='contribution')
router.register('job_offers', views.JobOfferViewSet, basename='job_offer')
router.register('applications', views.ApplicationViewSet, basename='application')

# URL patterns
urlpatterns = [
    # Administration
    path('admin/', admin.site.urls),

    # Accueil
    path('', views.home, name='home'),

    # API de base
    path('api/', views.api_home, name='api_home'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Gestion des événements
    path('events/', views.event_list, name='event_list'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/<int:pk>/delete/', views.event_delete, name='event_delete'),

    # Page de connexion
    path('connexion/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('connexion/', LoginView.as_view(template_name='core/login.html'), name='connexion'),

    # Page d'inscription
    path('inscription/', views.inscription, name='register'),
    path('profile/update/', views.update_profile, name='update_profile'),  # Assure-toi que cette ligne existe

    # Tableau de Bord
    path('dashboard/', views.dashboard, name='dashboard'),

    # Page de déconnexion
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Gestion des contributions
    path('api/contributions/', views.contribution_list, name='contribution_list'),  # API JSON
    path('contributions/view/', views.contribution_list_view, name='contribution_list_view'),  # Vue HTML
    path('contributions/', views.contribution_list, name='contribution_list'),
    path('contributions/add/', views.contribution_add, name='contribution_add'),
    path('contributions/<int:pk>/edit/', views.contribution_edit, name='contribution_edit'),
    path('contributions/<int:pk>/delete/', views.contribution_delete, name='contribution_delete'),


    # Gestion des offres d'emploi et des candidatures
    path('job_offers/', views.job_offer_list, name='job_offer_list'),
    path('job_offers/<int:offer_id>/', views.joboffer_detail, name='joboffer_detail'),


    path('applications/', views.application_list, name='application_list'),

path('members/', views.member_list, name='member_list'),
    path('members/<int:pk>/', views.member_detail, name='member_detail'),
    path('members/create/', views.member_create, name='member_create'),
    path('members/<int:pk>/delete/', views.member_delete, name='member_delete'),
    path('members/<int:pk>/', views.member_detail, name='member_detail'),
    path('members/<int:pk>/edit/', views.member_edit, name='member_edit'),


]
