from django.shortcuts import render
import random
# Create your views here.

def home(request) :
    return render(request, "index.html")

def result(request) :
    gamenum = int(request.GET['gamenum'])
    results = []
    for i in range(gamenum):
        results.append(random.sample(range(45),7))
    context = {
        "result" : results,
        "number" : gamenum
    }
    return render(request, "result.html", context)