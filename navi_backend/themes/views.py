from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ThemeCreateSerializer, ThemeDetailSerializer
from .models import Theme
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def create(request):

    serializer = ThemeCreateSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        theme = serializer.save()

    data = {
        'theme_id': theme.id,
    }
    return Response(data)


@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, theme_id):
    theme = get_object_or_404(Theme, id=theme_id)

    if request.method == 'GET':
        serializer = ThemeDetailSerializer(theme)
        data = {
            'theme': serializer.data,
        }
        return Response(data)

    elif request.method == 'PUT':
        # 권한 설정에 대한 코드가 필요합니다.
        serializer = ThemeCreateSerializer(theme, data=request.data)
        if serializer.is_valid(raise_exception=True):
            theme = serializer.save()
        data = {
            'theme_id': theme.id,
        }
        return Response(data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        # 권한 설정에 대한 코드가 필요합니다.
        theme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
