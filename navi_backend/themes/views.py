from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def create(request):
    print('test')
    data = {
        'test': 'test',
    }
    return Response(data)

