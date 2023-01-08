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
    data = {
        'kakao_login_url': url,
    }
    return Response(data)

cookie_lst = ['access', 'refresh']

@api_view(['POST'])
def login(request):
    auth_code = request.data.get('code')
    access_token = KakakoLogin.get_token(auth_code)
    kakako_profile = KakakoLogin.get_kakao_profile(access_token)

    token = KakakoLogin.jwt_create(kakako_profile, access_token)
    data = {'message': 'set_token'}
    res = Response(data, status=status.HTTP_200_OK)

    for key in cookie_lst:
        res.set_cookie(key=key, value=token.get(key), httponly=True)
    return res


@api_view(['POST'])
def logout(requset):
    data = {'message': 'logout'}
    res = Response(data)
    for key in cookie_lst:
        res.delete_cookie(key)
    return res


@api_view(['DELETE'])
def kakaoDelete(request):
    user = request.user
    if user.is_authenticated:
        KakakoLogin.unlink(user)
        user.delete()
        data = {
            'delete_account': '회원탈퇴가 완료되었습니다.'
        }
        res = Response(data, status=status.HTTP_204_NO_CONTENT)
        for key in cookie_lst:
            res.delete_cookie(key)
    return res
