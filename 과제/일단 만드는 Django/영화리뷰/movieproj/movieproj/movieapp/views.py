from django.shortcuts import render
import requests # pip install requests
import json
from .forms import SearchForm

my_id = '1b014a82ba5f09766125ca52e929b469'

def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        searchword = request.POST.get('search')
        if form.is_valid():
        # 압력된 검색어를 바탕으로
        # https://api.themoviedb.org/3/search/movie?api_key=1b014a82ba5f09766125ca52e929b469&language=en-US&page=1&include_adult=false
        # 로 get 요청 보내기 
            url = 'https://api.themoviedb.org/3/search/movie?api_key='+ my_id + '&query=' + searchword
            response = requests.get(url)
            resdata = response.text
            obj = json.loads(resdata)
            obj = obj['results']
            return render(request,'search.html',{'obj':obj})
    else :
        form = SearchForm()
        url = "https://api.themoviedb.org/3/trending/movie/week?api_key=" + my_id
        response = requests.get(url) # reponse 객체
        resdata = response.text
        # reponse객체의 문자열 -> json파일 
        # https://jsonformatter.curiousconcept.com/ 에 들어가서 보기 쉽게 가공 가능
        obj = json.loads(resdata) # python에서 가공하기 위해서 가져옴
        obj = obj['results']
    return render(request,'index.html',{'obj':obj,'form':form})

def detail(request, movie_id) :
    url = 'https://api.themoviedb.org/3/movie/'+ movie_id + '?api_key=' + my_id
    # https://api.themoviedb.org/3/movie/{movie_id}?api_key=1b014a82ba5f09766125ca52e929b469
    # 위 url에 get 요청 보내기 
    response = requests.get(url)
    resdata = response.text
    return render(request,'detail.html',{'resdata':resdata})

