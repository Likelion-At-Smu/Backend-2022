from django.shortcuts import render
import random

def lotto(request):
    return render(request, 'lotto.html')

def result(request):
    try:
        num  = int(request.GET['num'])
        total=[]
        for j in range(num):
            case=[]
            for i in range(7):
                case.append(random.randint(1,45))
            total.append(case)
        return render(request, 'result.html', {'num':num, 'total':total})
    except ValueError:
        return render(request, 'error.html')
    