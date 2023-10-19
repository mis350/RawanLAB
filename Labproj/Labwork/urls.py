from django.urls import path
from Labwork.views import rawan_view

urlpatterns = [
    path('rv/', rawan_view),
]
