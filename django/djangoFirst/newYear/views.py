from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    today = datetime.datetime.now()
    result = False
    if (today.month == 1 and today.day == 1):
        result = True
    return render(request, 'index.html',{
        'result': result
    })