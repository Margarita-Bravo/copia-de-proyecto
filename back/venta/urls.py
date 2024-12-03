from django.urls import path, include
from rest_framework import routers
from .views import ReferenceMPView


urlpatterns = [
    path('preference', ReferenceMPView.as_view()),
]
