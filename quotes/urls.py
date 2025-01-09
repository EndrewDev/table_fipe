from django.urls import path
from . import views

urlpatterns = [
    path(
        '', views.home, name='pagina-inicila'
    ),
    path(
        'brand/', views.brand, name='brands'
    ),
]
