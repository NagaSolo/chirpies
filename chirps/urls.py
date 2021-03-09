from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chirp-home'),
    path('about/', views.about, name='chirp-about'),
]