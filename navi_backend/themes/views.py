from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ThemeCreateSerializer, ThemeListSerializer
from .models import Theme

@api_view(['POST'])
def create(request):

    serializer = ThemeCreateSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        theme = serializer.save()

    data = {
        'theme_id': theme.id,
    }
    return Response(data)


@api_view(['GET'])
def theme_list(request, list_name):
    if list_name == 'latest':
        themes = Theme.objects.all().order_by('created')

    # 좋아요가 많은 순으로 출력
    # elif(list_name == 'popular'):
    #     themes = Theme.objects.all().order_by('theme_likes')

    else:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ThemeListSerializer(themes, many=True)

    data = {
        'themes': serializer.data
    }

    return Response(data)