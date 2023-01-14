from django.urls import path, include

from accounts import views


urlpatterns = [
    path('kakao/login/getcode/', views.kakaoGetcode),  # 카카오 코드 요청
    path('kakao/login/gettoken/', views.login),  # 카카오 로그인 요청
    path('kakao/delete/', views.kakaoDelete),  # 카카오 회원탈퇴
    path('logout/', views.logout),  # 카카오 회원탈퇴
]
