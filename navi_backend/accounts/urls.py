from django.urls import path, include

from accounts import views


urlpatterns = [
    path('kakao/login/getcode/', views.kakaoGetcode),  # 카카오 로그인
    path('kakao/login/redirect_uri/', views.login),  # 카카오 로그인 내부 로직용
    path('kakao/delete/', views.kakaoDelete),  # 카카오 회원탈퇴
    path('logout/', views.logout),  # 카카오 회원탈퇴
]
