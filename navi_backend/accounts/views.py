import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from django.conf import settings
# Create your views here.


@api_view(['GET'])
def kakaoGetcode(request):
    # Step 1: 인가 코드 받기
    client_id = settings.KAKAO_APP_CONFIG.get('REST_API_KEY')
    redirect_uri = settings.KAKAO_APP_CONFIG.get('REDIRECT_URI')
    url = f'https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code'
    return redirect(url)


@api_view(['GET'])
def getUserInfo(request):
    KAKAO_APP_CONFIG = settings.KAKAO_APP_CONFIG

    # Step 2: 토큰 받기
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

    # Step 3: 사용자 로그인 처리
    kakao_userinfo_api = 'https://kapi.kakao.com/v2/user/me'
    access_token = token_response.json().get('access_token')
    kakao_userinfo_headers = {'Authorization': f'Bearer {access_token}'}

    user_info = requests.get(kakao_userinfo_api, headers=kakao_userinfo_headers)

    # 회원가입

    # 로그인
    
    return Response(user_info.json())

# token_response = {
# "access_token": "1hmix1GjNob4qeMCo-y8FF_i-FBTntkGFai10x78Cj102wAAAYU-Cdhr",
# "token_type":"bearer",
# "refresh_token":"RgjzP6UNWbyRv8IXjwsi2VuE82BdePirzLCZ_29RCj102wAAAYU-Cdhp",
# "expires_in":21599,
# "scope":"account_email profile_image profile_nickname",
# "refresh_token_expires_in":5183999
# }
