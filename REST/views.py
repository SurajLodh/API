from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

class PersonView(APIView):

    def get(self, request, format=None):
    #1 Data
        A = {"date" : 'January',"High" : 47,"Low" : 27}
        B = {"date" : 'Fabruary',"High" : 47,"Low" : 25}
        C = {"date" : 'March',"High" : 53,"Low" : 21}
        
        Temp_Data = [A,B,C]
        
        data = {"Temp_Data": Temp_Data}
        return Response(data) 