from rest_framework import serializers
from .models import Place, Review, Place_Theme

class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = "__all__"

class PlaceThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place_Theme
        fields = "__all__"
        read_only_fields = ("user",)

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ("user",)
    
