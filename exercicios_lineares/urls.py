from django.urls import path
from .views import ExercicioAPIView

urlpatterns = [
    path('lineares/', ExercicioAPIView, name='lineares')
]