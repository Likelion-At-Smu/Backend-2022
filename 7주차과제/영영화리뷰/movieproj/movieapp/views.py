from django.shortcuts import render
import requests
import json
from .forms import SearchForm

my_id='944f54dccf061a028aab24a94c131c0b'
def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        searchword = request.POST.get('search')
        if form.is_valid():
            #입력된 내용을 바탕으로  url로 get 요청 보내기
            url = 'https://api.themoviedb.org/3/search/movie?api_key='+my_id+'&query='+searchword
            response=requests.get(url)
            resdata= response.text
            obj= json.loads(resdata)
            obj = obj['results']
            return render(request, 'search.html', {'obj':obj})
    else:
        form = SearchForm()
        url = 'https://api.themoviedb.org/3/trending/movie/week?api_key='+my_id
        response = requests.get(url) #pip install requests
        resdata = response.text #response 안에 있는 문자열 객체 접근하기 위해서
        #json 객체를 파이썬 객체로 반환하기 위해서(jsonformatter)
        obj= json.loads(resdata)
        obj = obj['results']
    return render(request, 'index.html', {'obj':obj, 'form':form})

def detail(request, movie_id):
    # https://api.themoviedb.org/3/movie/{movie_id}?api_key=944f54dccf061a028aab24a94c131c0b&language=en-US
    # 이 url에 get 요청 보내기
    url = 'https://api.themoviedb.org/3/movie/'+ movie_id +'?api_key='+my_id
    response = requests.get(url)
    resdata = response.text
    return render(request, 'detail.html', {'resdata':resdata})