from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_main(request):
    return render(request, 'mainapp/main.html')