from django.shortcuts import render
import requests
import json
from .forms import SearchForm
# forms 안에 있는 SearchForm을 가져온다     
my_id = '699ac4e672a90bf6cdff5aee97d024eb'

def home(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        # search로써  입력한 값을  POST request로 온 데이터중에서
        #  search로 입력된 값을 갖고 오겠다
        searchword = request.POST.get('search')
        if form.is_valid():  #만약 form으로 가져온 값이 적절하다면 
            url = 'https://api.themoviedb.org/3/search/movie?api_key=' +my_id+'&query='+searchword
            #그리고 이 url에 get요청을 보내면 된다
            response = requests.get(url)
            #그리고 응답 객체 response로 받아온 다음에
            resdata = response.text 
            #응답 객체 안에 있는 .text를 통해서 갖고오고자 하는 정보를 가져와서
            obj = json.loads(resdata)
            #responsde의 데어터 reesdata를 json 파일로 load해라
            obj = obj['results'] 
            #obj안에 obj에 result라고 하는 매칭 되는 값을 다시 넣어준다
            
            return render(request, 'search.html', {'obj':obj})
        #입력된 내용을 바탕으로
        #https://api.themoviedb.org/3/search/movie?api_key=699ac4e672a90bf6cdff5aee97d024eb
        #위 형태의 url로 get 요청 보내기
    else:
        form = SearchForm()
        #입력 할 수 있는 공간 SearchForm()을 찍어준다
        url = 'https://api.themoviedb.org/3/trending/all/day?api_key=' + my_id
        #패키지 형식으로 다운된다
        response = requests.get(url)
        resdata = response.text # 응답개체를 받아와서 resdata에 넣는다
        #문자열에 접근하기 위해서는 
        obj = json.loads(resdata)
        #위 resdata 자체는 json 이므로 json을 파이썬 객체로 반환해주기 위해서
        obj = obj['results']
        #json formatter로 확인시 우리가 가져오고자하는 데이터는 results이므로
    return render(request, 'index.html',{'obj':obj, 'form':form})
    #입력 받은 SearchForm을 index.html로 redering 해준다

def detail(request, movie_id):
    url = 'https://api.themoviedb.org/3/movie/' + movie_id  +'?api_key=' +my_id
    # 이 url에 get 요청 보내기
    response = requests.get(url)
    resdata = response.text
    return render(request, 'detail.html', {"resdata":resdata})