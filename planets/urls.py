# myapp/urls.py
from django.urls import path
from .views import PlanetView

urlpatterns = [
    path('planet/', PlanetView.as_view(), name='planet-list-create'),
]
