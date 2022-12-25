from django.urls import path, include

from accounts import views


urlpatterns = [
    path('kakao/login/getcode/', views.kakaoGetcode),
    path('kakao/login/redirect_uri/', views.login),
]
