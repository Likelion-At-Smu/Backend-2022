from django.shortcuts import render
import random

# Create your views here.
def lotto(request) :
    return render(request, 'index.html')

def result(request) :
    # 예외처리를 통해 
    try :
        # request.GET['count']를 통해 'GET'요청으로 들어온 count라는 파라미터를 받아 int형태로 저장
        count = int(request.GET['count']) 
        mylotto = []
        while len(mylotto) < count : 
            lottoNumber = random.sample(range(1,46),6) # random.sample을 이용하여 1~45사이의 수를 중복 없이 6개 뽑음
            mylotto.append(lottoNumber)

        return render(request, 'result.html',{'count':count,'mylotto':mylotto})
        
    except ValueError :
        print('숫자를 입력하십시오!')
        return render(request, 'index.html')