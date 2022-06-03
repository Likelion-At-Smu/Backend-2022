from django.shortcuts import render
import requests
import json
from .forms import SearchForm

# Create your views here.
# 모든 페이지에서 사용할 api
my_id = 'bf526943389bc922a21b53562e7d741b'

# 홈화면
def home(request):
    # POST
    if request.method == "POST":
        form = SearchForm(request.POST)
        # 입력한 값 가져오기
        searchword = request.POST.get('search')
        # 유효한 값이라면
        if form.is_valid():
            # 입력된 내용을 바탕으로 url로 get요청 보내기
            url = 'https://api.themoviedb.org/3/search/movie?api_key='+my_id+'&query='+searchword
            response = requests.get(url)
            resdata = response.text
            obj = json.loads(resdata)
            obj = obj['results']
            return render(request, 'search.html',{'resdata':obj})
        
    # GET
    else:
        form = SearchForm()
        # request를 보내야 하는 url
        url = 'https://api.themoviedb.org/3/trending/all/day?api_key='+my_id
        # 반환받은 response객체
        response = requests.get(url)
        # 우리가 가공해서 사용하는 정보
        resdata = response.text
        # json을 python 객체로 바꾸기
        obj = json.loads(resdata)
        # 영화들의 정보만 사용할것
        # 리스트 형태이기 떄문에 temlplate을 이용해 순회 가능
        obj = obj['results']

        return render(request, 'index.html', {'resdata' : obj, 'form' : form})

def detail(request, movie_id):
    url = "https://api.themoviedb.org/3/movie/"+movie_id+"?api_key="+my_id
    response = requests.get(url)
    resdata = response.text
    obj = json.loads(resdata)
    return render(request, 'detail.html', {"resdata" : obj})
