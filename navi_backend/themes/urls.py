from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create),
    path('list/<str:list_name>/', views.theme_list),
]
