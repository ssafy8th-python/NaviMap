from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create),

    path('weather/<str:lat>/<str:lon>/', views.weather),
]
