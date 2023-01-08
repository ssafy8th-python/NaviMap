from sys import platlibdir
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Place, Place_Theme, Review
from themes.models import Theme, Tag
from .serializers import PlaceSerializer, PlaceThemeSerializer, ReviewSerializer
from django.contrib.auth import get_user_model

# Create your views here.
@api_view(['GET'])
def place_theme_list(request, theme_id):
    theme = Theme.objects.get(id=theme_id)
    places = theme.places.all()
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def place_list(request, place_id):
    places = Place_Theme.objects.filter(place_id=place_id)
    serializer = PlaceThemeSerializer(places, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_place_theme(request, theme_id):
    place, is_created = Place.objects.get_or_create(
        kakao_id=request.data['kakao_id'],
        defaults={
            'name': request.data['name'],
            'address': request.data['address'],
            'x_label': request.data['x_label'],
            'y_label': request.data['y_label']
        }
    )
    theme = Theme.objects.get(id=theme_id)

    serializer = PlaceThemeSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, place=place, theme=theme)
        place_theme = Place_Theme.objects.get(id=serializer.data['id'])
        
        for tag_name in request.data['tags']:
            if not place_theme.tags.filter(tag_name=tag_name).exists():
                tag = Tag.objects.get(tag_name=tag_name)
                place_theme.add(tag.id)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def get_or_create_review(request, place_id):
    place = Place.objects.get(id=place_id)
    if request.method == "GET":
        reviews = Review.objects.filter(place_id=place_id)
        serializer = ReviewSerializer(reviews, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, place=place)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def update_or_delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)