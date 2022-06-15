from django.urls import path
from .views import ExercicioAPIView

urlpatterns = [
    path('exercicio/', ExercicioAPIView, name='exercicios')
]