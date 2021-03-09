from django.urls import path

from . import views

from .views import (
    ChirpListView, 
    ChirpDetailView, 
    ChirpCreateView, 
    ChirpUpdateView,
    ChirpDeleteView,
    UserChirpListView
)
urlpatterns = [
    path('', views.home, name='chirp-home'),
    path('about/', views.about, name='chirp-about'),
    path('user/<str:username>', UserChirpListView.as_view(), name='user-chirps'),
    path('chirp/<int:pk>/', ChirpDetailView.as_view(), name='chirp-detail'), # grab specific primary key of chirp
    path('chirp/new/', ChirpCreateView.as_view(), name='chirp-create'), # create new chirp
    path('chirp/<int:pk>/update/', ChirpUpdateView.as_view(), name='chirp-update'), # update specific chirp
    path('chirp/<int:pk>/delete/', ChirpDeleteView.as_view(), name='chirp-delete'), # delete specific chirp
]