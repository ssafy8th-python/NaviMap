import requests

from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.conf import settings
from django.contrib.auth import get_user_model

from .serializers import UserCreateSerializer

class KakakoLogin:
    # 카카오 앱 키
    KAKAO_APP_CONFIG = settings.KAKAO_APP_CONFIG


    def get_token(auth_code):
        '''
        카카오톡에 사용자 정보를 요청하기 위한 access token 발급;

        auth_code: 카카오톡에서 발급한 인가코드;
        '''
        kakao_token_api = 'https://kauth.kakao.com/oauth/token'
        k_config = KakakoLogin.KAKAO_APP_CONFIG
        throw_token_data = {
            'grant_type': 'authorization_code',
            'client_id': k_config.get('REST_API_KEY'),
            'redirect_uri': k_config.get('REDIRECT_URI'),
            'code': auth_code,
            'client_secret': k_config.get('CLIENT_SECRET'),
        }
        return requests.post(kakao_token_api, data=throw_token_data).json().get('access_token')


    def get_kakao_profile(access_token):
        '''
        카카오톡에 사용자 정보 요청

        참고 링크: https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#req-user-info-response
        '''
        kakao_userinfo_api = 'https://kapi.kakao.com/v2/user/me'
        kakao_userinfo_headers = {'Authorization': f'Bearer {access_token}'}

        return requests.get(kakao_userinfo_api, headers=kakao_userinfo_headers).json()


    def jwt_create(kakako_profile):
        '''
        기존 사용자: simple-jwt로 바로 jwt 발급

        새로운 사용자: 회원가입 후 simple-jwt로 jwt 발급
        '''
        kakao_id = kakako_profile.get('id')
        kakao_account = kakako_profile.get('kakao_account')
        profile = kakao_account.get('profile')
        User = get_user_model()

        try:
            user = User.objects.get(pk=kakako_profile.get('id'))

        # 회원가입
        except User.DoesNotExist:
            serializer = UserCreateSerializer(data={'username': kakao_id,})
            if serializer.is_valid(raise_exception=True):
                user = serializer.save(id=kakao_id)
                user.set_password(f'{kakao_id}password')
                user.save()

        # 회원정보 업데이트
        user.nickname = profile.get('nickname')
        user.profile_image = profile.get('profile_image_url')
        user.thumbnail_image = profile.get('thumbnail_image_url')
        user.email = kakao_account.get('email')
        user.save()

        # jwt 발급
        jwt_data = {'username': kakao_id, 'password': f'{kakao_id}password',}
        serializer = TokenObtainPairSerializer(data=jwt_data)
        if serializer.is_valid(raise_exception=True):
            jwt = serializer.validated_data
            user.refresh_token = jwt.get('refresh')
            user.save()

        return jwt