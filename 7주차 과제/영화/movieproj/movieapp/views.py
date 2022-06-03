import json

from django.shortcuts import render
import requests

my_key = '6db58df2eccf67c069d7e714d4681465'

def home(request):
    # forms.py를 생성하지 않고 html form을 만들어서 검색 구현
    if request.method == 'POST':
        query = request.POST['query']
        url = 'https://api.themoviedb.org/3/search/movie?api_key=' + my_key + '&language=en-US&query=' + query + '&page=1&include_adult=false'
        response = requests.get(url)
        resdata = response.text
        obj = json.loads(resdata)

    else:
        url = 'https://api.themoviedb.org/3/trending/movie/week?api_key=' + my_key
        #requests 라이버르리를 사용하여 api url의 정보를 받아서 저장
        response = requests.get(url)
        #일반 객체를 text 형식으로 형변환
        #json 포맷의 텍스트를 jsonformatter에 붙여넣으면 보기 좋게 정리해줌
        resdata = response.text
        #txt 형식의 정보를 json형식으로 변경
        obj = json.loads(resdata)
    return render(request, 'index.html', {'obj':obj['results']})

def detail(request, movie_id):
    #findbyid try it out 에서 예시 링크를 응용
    url = 'https://api.themoviedb.org/3/movie/'+movie_id+'?api_key='+my_key
    response = requests.get(url)
    resdata = response.text
    detail = json.loads(resdata)

    return render(request, 'detail.html', {'detail': detail})

#forms.py를 생성하지 않고 html form을 만들어서 검색 하는 함수
# def search(request):
#     query = request.POST['query']
#     url = 'https://api.themoviedb.org/3/search/movie?api_key='+my_key+'&language=en-US&query='+query+'&page=1&include_adult=false'
#     response = requests.get(url)
#     resdata = response.text
#     search_info = json.loads(resdata)
#
#     return render(request, 'search.html',{'search_info':search_info})
# Create your views here.
