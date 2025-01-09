from django.urls import path
from . import views

urlpatterns = [
    path(
        '', views.home, name='pagina-inicila'
    ),
    path(
        'brand/', views.brand, name='brands'
    ),
    path(
        "models/", views.models, name="models"
    ),
    path(
        "yearmdoel/", views.models_years, name="vehicle-value"
    ),
]
