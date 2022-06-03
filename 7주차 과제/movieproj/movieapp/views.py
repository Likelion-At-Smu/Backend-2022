from django.shortcuts import render
import requests
import json
from .forms import SearchForm

my_id = 'b55903487166ddfd57c550de36298cf6'

def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        searchword = request.POST.get('search')
        if form.is_valid():
            url = 'https://api.themoviedb.org/3/search/movie?api_key='+my_id+'&query='+searchword
            #입력받은 값을 기반으로 위 url로 검색결과를 보낸다.
            response = requests.get(url)#반환 받는 값. 응답 객체 그자체
            resdata = response.text#객체의 텍스트, 정보
            obj = json.loads(resdata)#json을 파이썬 객체로 변환한다.
            obj = obj['results']
            return render(request, 'search.html', {'obj':obj})#obj로 반환
    else:
        form = SearchForm()
        url = 'https://api.themoviedb.org/3/trending/movie/week?api_key='+my_id
        response = requests.get(url)
        resdata = response.text
        obj = json.loads(resdata)
        obj = obj['results']
    return render(request, 'index.html', {'obj':obj, 'form':form})

def detail(request, movie_id):

    url = 'https://api.themoviedb.org/3/movie/' + movie_id +'?api_key='+my_id
    response = requests.get(url)
    resdata = response.text
    resdata = json.loads(resdata)
    return render(request, 'detail.html', {"resdata":resdata})