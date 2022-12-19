from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ThemeCreateSerializer

@api_view(['POST'])
def create(request):

    serializer = ThemeCreateSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        theme = serializer.save()

    data = {
        'theme_id': theme.id,
    }
    return Response(data)

