from django.urls import path
from . import views

urlpatterns = [
    path('project/add/', views.project_add, name='pages_project_add'),
]
