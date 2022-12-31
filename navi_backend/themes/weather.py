import math, requests, json
from datetime import date, timedelta
from django.core.cache import cache
import datetime, os


NX = 149            ## X축 격자점 수
NY = 253            ## Y축 격자점 수

Re = 6371.00877     ##  지도반경
grid = 5.0          ##  격자간격 (km)
slat1 = 30.0        ##  표준위도 1
slat2 = 60.0        ##  표준위도 2
olon = 126.0        ##  기준점 경도
olat = 38.0         ##  기준점 위도
xo = 210 / grid     ##  기준점 X좌표
yo = 675 / grid     ##  기준점 Y좌표
first = 0

if first == 0 :
    PI = math.asin(1.0) * 2.0
    DEGRAD = PI/ 180.0
    RADDEG = 180.0 / PI


    re = Re / grid
    slat1 = slat1 * DEGRAD
    slat2 = slat2 * DEGRAD
    olon = olon * DEGRAD
    olat = olat * DEGRAD

    sn = math.tan(PI * 0.25 + slat2 * 0.5) / math.tan(PI * 0.25 + slat1 * 0.5)
    sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
    sf = math.tan(PI * 0.25 + slat1 * 0.5)
    sf = math.pow(sf, sn) * math.cos(slat1) / sn
    ro = math.tan(PI * 0.25 + olat * 0.5)
    ro = re * sf / math.pow(ro, sn)
    first = 1

def mapToGrid(lat, lon, code = 0 ):
    ra = math.tan(PI * 0.25 + lat * DEGRAD * 0.5)
    ra = re * sf / pow(ra, sn)
    theta = lon * DEGRAD - olon
    if theta > PI :
        theta -= 2.0 * PI
    if theta < -PI :
        theta += 2.0 * PI
    theta *= sn
    x = (ra * math.sin(theta)) + xo
    y = (ro - ra * math.cos(theta)) + yo
    x = int(x + 1.5)
    y = int(y + 1.5)
    return x, y

def gridToMap(x, y, code = 1):
    x = x - 1
    y = y - 1
    xn = x - xo
    yn = ro - y + yo
    ra = math.sqrt(xn * xn + yn * yn)
    if sn < 0.0 :
        ra = -ra
    alat = math.pow((re * sf / ra), (1.0 / sn))
    alat = 2.0 * math.atan(alat) - PI * 0.5
    if math.fabs(xn) <= 0.0 :
        theta = 0.0
    else :
        if math.fabs(yn) <= 0.0 :
            theta = PI * 0.5
            if xn < 0.0 :
                theta = -theta
        else :
            theta = math.atan2(xn, yn)
    alon = theta / sn + olon
    lat = alat * RADDEG
    lon = alon * RADDEG

    return lat, lon
    
def getWeather(lat, lon):

    # 캐시에 대한 코드
    # tmp_lat = lat.split('.')[0]
    # tmp_lon = lon.split('.')[0]

    # location = 'location'+tmp_lat+'_'+tmp_lon

    # weather = cache.get(location)

    # if weather:
    #     cloud, precipitation = weather
    #     # cache.delete(location)

    #     return cloud, precipitation

    lat = float(lat)
    lon = float(lon)

    # 시간 설정
    yesterday = date.today() - timedelta(1)
    now = datetime.datetime.now()
    fcstDate = now.strftime("%Y%m%d")
    base_date = yesterday.strftime("%Y%m%d")
    base_time = "0200"
    fcstTime = now.strftime("%H") + "00"
    hour = now.hour

    if hour >= 23:
        base_time = "2300"
    elif hour >= 20:
        base_time = "2000"
    elif hour >= 17:
        base_time = "1700"
    elif hour >= 14:
        base_time = "1400"
    elif hour >= 11:
        base_time = "1100"
    elif hour >= 8:
        base_time = "0800"
    elif hour >= 5:
        base_time = "0500"

    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
    
    # 위도, 경도
    x, y = mapToGrid(float(lat), float(lon))
    WEATHER_SECRET_KEY = os.environ.get('WEATHER_SECRET_KEY')
    params ={'serviceKey' : WEATHER_SECRET_KEY, 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'JSON', 'base_date' : base_date, 'base_time' : base_time, 'nx' : x, 'ny' : y }

    response = requests.get(url, params=params)
    content = response.content
    json_object = json.loads(content)
    weathers = json_object['response']['body']['items']['item']

    for weather in weathers:
        if weather['fcstTime'] == fcstTime and weather['fcstDate'] == fcstDate:
            if weather['category'] == 'SKY':
                if weather['fcstValue'] == '1':
                    cloud = "맑음"
                elif weather['fcstValue'] == '3':
                    cloud = "구름많음"
                elif weather['fcstValue'] == '4':
                    cloud = "흐림"

            if weather['category'] == 'PTY':
                # precipitation 강수 형태
                precipitation = "없음"

                if weather['fcstValue'] == '1':
                    precipitation = "비"
                elif weather['fcstValue'] == '2':
                    precipitation = "비눈"
                elif weather['fcstValue'] == '3':
                    precipitation = "눈"
                elif weather['fcstValue'] == '4':
                    precipitation = "소나기"
    # 캐시에 대한 코드
    # cache.set(location, (cloud, precipitation), 3600)
    return cloud, precipitation

    