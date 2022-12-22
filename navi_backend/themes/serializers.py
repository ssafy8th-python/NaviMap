from rest_framework import serializers
from .models import Theme

class ThemeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = '__all__'
        read_only_fields = ('theme_creator', 'theme_tags', 'theme_likes')


class MainPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = '__all__'
        read_only_fields = ('theme_creator', 'theme_tags')


class ThemeDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = '__all__'


class ThemeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        exclude = ('is_update', )
