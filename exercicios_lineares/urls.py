from django.urls import path
from .views import LinearAPIView

urlpatterns = [
    path('linear/', LinearAPIView.as_view())
]
