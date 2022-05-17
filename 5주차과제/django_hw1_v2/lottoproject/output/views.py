from django.shortcuts import render
import random
# Create your views here.
def output(request):
    try:
        num  = int(request.GET['num'])
        total=[]
        for j in range(num):
            case=[]
            for i in range(7):
                case.append(random.randint(1,45))
            total.append(case)
        return render(request, 'output.html', {'num':num, 'total':total})
    except ValueError:
        return render(request, 'error.html')
 