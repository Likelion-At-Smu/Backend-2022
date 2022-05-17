from django.shortcuts import render

def home(request):
    import random
    count = int(request.GET.get('count'))
    numlist = list(range(1,46))
    result= []
    for i in range(count):
        number = random.sample(numlist, 6)
        result.append(number)
    context= {
        'count' : count,
        'result' : result
    }
    return render(request, 'result.html', context)
