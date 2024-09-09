from django.urls import path
from .views import HomePageView

#Definiendo la url para el HTML
urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]