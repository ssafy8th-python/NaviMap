import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from django.conf import settings
# Create your views here.


@api_view(['GET'])
def kakaoGetcode(request):
    client_id = settings.KAKAO_APP_CONFIG.get('REST_API_KEY')
    redirect_uri = settings.KAKAO_APP_CONFIG.get('REDIRECT_URI')
    url = f'https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code'
    return redirect(url)


@api_view(['GET'])
def getUserInfo(request):
    KAKAO_APP_CONFIG = settings.KAKAO_APP_CONFIG
    auth_code = request.GET.get('code')
    kakao_token_api = 'https://kauth.kakao.com/oauth/token'
    throw_token_data = {
        'grant_type': 'authorization_code',
        'client_id': KAKAO_APP_CONFIG.get('REST_API_KEY'),
        'redirect_uri': KAKAO_APP_CONFIG.get('REDIRECT_URI'),
        'code': auth_code,
        'client_secret': KAKAO_APP_CONFIG.get('CLIENT_SECRET'),
    }
    token_response = requests.post(kakao_token_api, data=throw_token_data)
    return Response(token_response)
