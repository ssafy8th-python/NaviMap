from rest_framework import serializers
from .models import Theme

class ThemeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theme
        fields = '__all__'

        read_only_fields = ('theme_creator', 'theme_tags')