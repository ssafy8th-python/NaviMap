from django.urls import path
from . import views

urlpatterns = [
    path('<int:theme_id>/create_place_theme/', views.create_place_theme),
    path('<int:place_id>/get_or_create_review/', views.get_or_create_review),
    path('<int:place_id>/update_or_delete_review/', views.update_or_delete_review),
    path('<int:theme_id>/place_theme_list/', views.place_theme_list),
    path('<int:theme_id>/place_list/', views.place_list),
]
