from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup



# Create your views here.
def home(request):
    return render(request, 'main/index.html')