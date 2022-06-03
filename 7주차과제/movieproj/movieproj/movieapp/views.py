from urllib import response
from django.shortcuts import render
import requests
import json
from .forms import SearchForm

my_id = 'c1c2d352fffa3dfce94cbba65b22f5ae'

def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        # searchword에 search한거 검색어 넘겨줌
        searchword = request.POST.get('search')
        # form의 값이 유효하다면
        if form.is_valid():
            url = 'https://api.themoviedb.org/3/search/movie?api_key=' + my_id + '&query=' + searchword
            response = requests.get(url)
            resdata = response.text
            obj = json.loads(resdata)
            obj = obj['results']
            return render(request, 'search.html', {'obj':obj})
        # 입력된 내용 바탕으로
        # https://api.themoviedb.org/3/search/movie?api_key=c1c2d352fffa3dfce94cbba65b22f5ae&language=en-US&query=hello&page=1&include_adult=false
        # 위 형태의 url로 get요청 보내기
        
    else:
        form = SearchForm()
        url = 'https://api.themoviedb.org/3/trending/movie/week?api_key=' + my_id
        response = requests.get(url)
        # response는 응답 객체 자체
        # .text는 우리가 가공하고자 하는 정보에 해당하는 것
        resdata = response.text
        
        # json을 파이썬으로 다루고자
        obj = json.loads(resdata)
        obj = obj['results']
    return render(request, 'index.html', {'obj':obj, 'form':form})

def detail(request, movie_id):
    url = 'https://api.themoviedb.org/3/movie/' + movie_id +'?api_key=' + my_id
    # https://api.themoviedb.org/3/movie/300?api_key=c1c2d352fffa3dfce94cbba65b22f5ae
    # 이 URL에 GET 요청 보내기

    response = requests.get(url)
    resdata = response.text
    resdata = json.loads(resdata)
    return render(request, 'detail.html', {'resdata':resdata})