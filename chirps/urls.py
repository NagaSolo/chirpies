from django.urls import path
from . import views

path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]