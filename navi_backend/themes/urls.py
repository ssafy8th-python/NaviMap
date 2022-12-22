from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create),
    path('<int:theme_id>/likes/', views.likes),
    path('<int:theme_id>/', views.detail),
    path('list/<str:list_name>/', views.theme_list),
    
    path('weather/<str:lat>/<str:lon>/', views.weather),
]
