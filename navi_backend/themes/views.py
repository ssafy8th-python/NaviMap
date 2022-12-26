#rest framework 관련
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# django 관련
from django.shortcuts import get_object_or_404
from django.db.models import Count
from .serializers import ThemeCreateSerializer, ThemeListSerializer, ThemeDetailSerializer, MainPageSerializer
from .models import Theme
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# 기타 api 관련
from .weather import getWeather
import datetime

theme_id_response = openapi.Response('int : theme_id')


@swagger_auto_schema(
    method='POST', 
    operation_description='''api 정보 : 테마를 생성합니다.''',
    request_body=ThemeCreateSerializer,
    responses={201: theme_id_response},
)
@api_view(['POST'])
def create(request):

    serializer = ThemeCreateSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        theme = serializer.save()

    data = {
        'theme_id': theme.id,
    }
    return Response(data)
    

@api_view(['GET'])
def mainpage(request, weather_data):
    latest_recos = Theme.objects.order_by('-created')[:6]
    popular_recos = Theme.objects.annotate(like_count=Count('theme_likes')).order_by('-like_count')[:6]
    

    # 오늘의 추천 3개 (날씨, 계절, 미세먼지 등 알고리즘 적용)
    today_recos = today_reco(weather_data)

    # 개인별 추천 3개 (좋아요한 테마와 비슷한 테마, 좋아요한 유저의 테마, 최근 검색한 테마와 비슷한 테마 등)
    # personal_recos = []

    latest_serializer = MainPageSerializer(latest_recos, many=True)
    popular_serializer = MainPageSerializer(popular_recos, many=True)
    today_serializer = MainPageSerializer(today_recos, many=True)
    # personal_serializer = MainPageSerializer(personal_recos, many=True)

    data = {
        'latest_recos': latest_serializer.data,
        'popular_recos': popular_serializer.data,
        'today_recos': today_serializer.data,
        # 'personal_recos': personal_serializer.data,
    }
    
    return Response(data)


# Test 필요
@api_view(['POST'])
def likes(request, theme_id):
    theme = Theme.objects.get(pk=theme_id)

    if theme.theme_likes.filter(pk=request.user.pk).exists():
        theme.theme_likes.remove(request.user)
        is_like = False
    else:
        theme.theme_likes.add(request.user)
        is_like = True
    
    data = {
        'is_like': is_like
    }
    
    return Response(data)


@swagger_auto_schema(
    method='GET', 
    operation_description='''api 정보 : 테마 상세페이지를 불러옵니다.
    theme_id : 테마 id를 입력해주세요. ''', 
    responses={200: ThemeDetailSerializer},
)
@swagger_auto_schema(
    method='PUT', 
    operation_description='''api 정보 : 테마 정보를 수정합니다.
    theme_id : 테마 id를 입력해주세요. ''', 
    responses={201: theme_id_response},
)
@swagger_auto_schema(
    method='DELETE', 
    operation_description='''api 정보 : 테마를 삭제합니다.
    theme_id : 테마 id를 입력해주세요. ''', 
)
@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, theme_id):
    theme = get_object_or_404(Theme, id=theme_id)

    if request.method == 'GET':
        serializer = ThemeDetailSerializer(theme)
        data = {
            'theme': serializer.data,
        }
        return Response(data)

    elif request.method == 'PUT':
        # 권한 설정에 대한 코드가 필요합니다.
        serializer = ThemeCreateSerializer(theme, data=request.data)
        if serializer.is_valid(raise_exception=True):
            theme = serializer.save()
        data = {
            'theme_id': theme.id,
        }
        return Response(data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        # 권한 설정에 대한 코드가 필요합니다.
        theme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(
    method='GET', 
    operation_description='''api 정보 : 테마 정보를 인기순 or 최신순으로 불러올 수 있습니다.
    list_name : latest or popular 값을 넣을 수 있습니다. ''', 
    responses={200: ThemeListSerializer(many=True)},
)
@api_view(['GET'])
def theme_list(request, list_name):
    if list_name == 'latest':
        themes = Theme.objects.all().order_by('-created')[:9]

    # 좋아요가 많은 순으로 출력
    elif(list_name == 'popular'):
        themes = Theme.objects.annotate(like_count=Count('theme_likes')).order_by('-like_count')[:9]

    else:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ThemeListSerializer(themes, many=True)

    data = {
        'themes': serializer.data
    }

    return Response(data)


@swagger_auto_schema(
    method='GET', 
    operation_description='''api 정보 : 현재 날씨 정보를 가져옵니다.
    lat : 위도를 입력해주세요.
    lon : 경도를 입력해주세요. ''', 
    responses={200: '''cloud : String
    precipitation : String'''},
)
@api_view(['GET'])
def weather(request, lat, lon):

    # cloud: 구름의 양, precipitation: 강수형태,  lat: 위도, lon: 경도
    # (tuple | tuple[Unbound | Literal['맑음', '구름많음', '흐림'], Unbound | Literal['비', '비눈', '눈', '소나기', '없음']])
    cloud, precipitation = getWeather(lat, lon)

    # print(cloud, precipitation)
    data = {
        'cloud': cloud,
        'precipitation': precipitation,
    }

    return Response(data)

def today_reco(weather_data):
    today_recos = []

    # 계절별 추천
    this_month = datetime.date.today().month

    # 임시태그 (tags의 pk가 담겨있어야함)
    SEASON_TAGS = {
        'spring': [1, 2, 3, 4], # ['따뜻한', '화려한', '포근한', '설레는'],
        'summer': [5, 6, 7, 8], # ['시원한', '신나는', '붐비는', '화끈한'],
        'autumn': [9, 10, 11, 12], # ['분위기 있는', '은은한', '차분한', '조용한'],
        'winter': [1, 3, 12, 13], # ['따뜻한', '포근한', '조용한', '안락한'],
    }

    if this_month in [3, 4, 5]: # 봄
        theme_season = Theme.objects.filter(
                theme_tags__in=SEASON_TAGS.get('spring')
            ).annotate(
                like_count=Count('theme_likes')
            ).order_by('-like_count')
        
    elif this_month in [6, 7, 8]: # 여름
        theme_season = Theme.objects.filter(
                theme_tags__in=SEASON_TAGS.get('summer')
            ).annotate(
                like_count=Count('theme_likes')
            ).order_by('-like_count')
    
    elif this_month in [9, 10, 11]: # 가을
        theme_season = Theme.objects.filter(
                theme_tags__in=SEASON_TAGS.get('autumn')
            ).annotate(
                like_count=Count('theme_likes')
            ).order_by('-like_count')
    
    elif this_month in [12, 1, 2]: # 겨울
        theme_season = Theme.objects.filter(
                theme_tags__in=SEASON_TAGS.get('winter')
            ).annotate(
                like_count=Count('theme_likes')
            ).order_by('-like_count')

    if theme_season:
        today_recos.append(theme_season[0])
    
    # 날씨별 추천
    cloud, precipitation = weather_data.get('cloud'), weather_data.get('precipitation')
    
    weather_tags = []

    if cloud == '맑음':
        weather_tags.extend([6,]) # [신나는] 등 태그 삽입
    elif cloud == '구름많음':
        weather_tags.extend([9, 15,]) # [분위기 있는, 조용한] 등 태그 삽입
    elif cloud == '흐림':
        weather_tags.extend([3, 13,]) # [포근한, 안락한] 등 태그 삽입

    if precipitation == '비':
        weather_tags.extend([9, 10, ]) # [분위기 있는, 은은한] 등 태그 삽입
    elif precipitation == '비눈':
        weather_tags.extend([1, 9, ]) # [따뜻한, 분위기 있는] 등 태그 삽입
    elif precipitation == '눈':
        weather_tags.extend([1, 3, 13, ]) # [따뜻한, 포근한, 안락한 ] 등 태그 삽입
    elif precipitation == '소나기':
        weather_tags.extend([11, 12,]) # [차분한, 조용한] 등 태그 삽입
    elif precipitation == '없음':
        weather_tags.extend([6, 7,]) # [신나는, 붐비는] 등 태그 삽입
    
    weather_tags = list(set(weather_tags))
    
    theme_weather = Theme.objects.filter(
            theme_tags__in=weather_tags
        ).annotate(
            like_count=Count('theme_likes')
        ).order_by('-like_count')

    if theme_weather:
        today_recos.append(theme_weather[0])
    
    return today_recos


def test(target):
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(target)
    print(type(target))
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@')