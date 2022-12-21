from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ThemeCreateSerializer
from .weather import getWeather


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
def weather(request, lat, lon):

    # cloud: 구름의 양, precipitation: 강수형태,  lat: 위도, lon: 경도
    cloud, precipitation = getWeather(float(lat), float(lon))

    # cloud
    print(cloud, precipitation)

