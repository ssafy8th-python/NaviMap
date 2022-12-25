from rest_framework import serializers

from django.contrib.auth import get_user_model

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'nickname', 'profile_image', 'thumbnail_image', 'email',)