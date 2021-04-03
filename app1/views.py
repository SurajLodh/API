from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404 

# Create your views here.

def Index(request):

    return render(request, 'index.html')
    # return HttpResponse("hello world")