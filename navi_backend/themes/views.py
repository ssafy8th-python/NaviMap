from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ThemeCreateSerializer, MainPageSerializer
from .models import Theme

@api_view(['POST'])
def create(request):

    serializer = ThemeCreateSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        theme = serializer.save()

    data = {
        'theme_id': theme.id,
    }
    return Response(data)




























































































def latest_theme_sort(themes):
    return sorted(themes, key=lambda x: x.created, reverse=True)


# 인기순 정렬을 위한 함수
# def popular_theme_sort(themes):
#     return sorted(themes, key=lambda x: x.theme_likes, reverse=True)


@api_view(['GET'])
def mainpage(request):
    themes = Theme.objects.all()
    latest_recos = latest_theme_sort(themes)[:6]
    
    # 메인페이지의 인기순 정렬 테마 6개
    # popular_recos = popular_theme_sort(themes)[:6]
    
    # 오늘의 추천 3개 (날씨, 계절, 미세먼지 등 알고리즘 적용)
    # today_recos = []

    # 개인별 추천 3개 (좋아요한 테마와 비슷한 테마, 좋아요한 유저의 테마, 최근 검색한 테마와 비슷한 테마 등)
    # personal_recos = []

    latest_serializer = MainPageSerializer(latest_recos, many=True)
    # popular_serializer = MainPageSerializer(popular_recos, many=True)
    # today_serializer = MainPageSerializer(today_recos, many=True)
    # personal_serializer = MainPageSerializer(personal_recos, many=True)

    context = {
        'latest_recos': latest_serializer.data,
        # 'popular_recos': popular_serializer.data,
        # 'today_recos': today_serializer.data,
        # 'personal_recos': personal_serializer.data,
    }
    
    return Response(context)