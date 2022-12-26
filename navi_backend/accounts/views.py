import requests

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404

from django.conf import settings
from django.shortcuts import redirect

from .logins import KakakoLogin
# Create your views here.


@api_view(['GET'])
def kakaoGetcode(request):
    # 인가 코드 받기
    client_id = settings.KAKAO_APP_CONFIG.get('REST_API_KEY')
    redirect_uri = settings.KAKAO_APP_CONFIG.get('REDIRECT_URI')
    url = f'https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code'
    return redirect(url)


@api_view(['GET'])
def login(request):
    auth_code = request.GET.get('code')
    access_token = KakakoLogin.get_token(auth_code)
    kakako_profile = KakakoLogin.get_kakao_profile(access_token)

    data = KakakoLogin.jwt_create(kakako_profile)
    return Response(data)
