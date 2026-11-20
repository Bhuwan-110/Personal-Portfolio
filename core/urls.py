from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('experience/', views.experience, name='experience'),
    path('achievements/', views.achievements, name='achievements'),
    path('projects/', views.projects, name='projects'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
    path('download-cv/', views.download_cv, name='download_cv'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
