from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Place, Place_Theme, Review
from themes.models import Theme, Tag
from .serializers import PlaceSerializer, PlaceThemeSerializer, ReviewSerializer
from django.contrib.auth import get_user_model

# Create your views here.

@api_view(['GET', 'POST'])
def get_or_create_place(request, theme_id):
    theme = Theme.objects.get(id=theme_id)
    if request.method == 'GET':
        place = Place.objects.filter(theme_id = theme_id)
        serializer = PlaceSerializer(place, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, themes=theme)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

def get_or_create_place_theme(request, place):
    