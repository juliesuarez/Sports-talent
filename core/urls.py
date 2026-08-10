from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Landing page
    path('', views.IndexView.as_view(), name='index'),

    # Dashboard and Management (Protected)
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('academy/add/', views.AcademyCreateView.as_view(), name='academy_add'),
    path('player/add/', views.PlayerCreateView.as_view(), name='player_add'),
    path('player/<int:pk>/edit/', views.PlayerUpdateView.as_view(), name='player_edit'),
    path('player/<int:pk>/delete/', views.PlayerDeleteView.as_view(), name='player_delete'),
    path('player/<int:pk>/transfer/', views.PlayerTransferView.as_view(), name='player_transfer'),

    # Authentication
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),

    # Super Admin & Directory
    path('directory/', views.SuperAdminDashboardView.as_view(), name='super_admin_dashboard'),
    path('academy/<int:pk>/', views.AcademyDetailView.as_view(), name='academy_detail'),
]