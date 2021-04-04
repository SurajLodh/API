from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
#implement
import pandas as pd
import numpy as np
import json
import os
from json import dumps

# Create your views here.

class PersonView(APIView):

    def get(self, request, format=None):
    #1 Data
        # A = {"date" : 'January',"High" : 47,"Low" : 27}
        # B = {"date" : 'Fabruary',"High" : 47,"Low" : 25}
        # C = {"date" : 'March',"High" : 53,"Low" : 21}
        
        # Temp_Data = [A,B,C]
        
        # data = {"Temp_Data": Temp_Data}

    #Implementing data
        os.chdir(r"C:\Users\suraj\Downloads\pc documents")
        os.getcwd()
        os.listdir()
        df = pd.read_csv('owid-covid-data.csv', encoding='utf-8', na_values=None, error_bad_lines=False)
        df = df.sort_values(by='total_vaccinations', ascending=False)

        df2 = df[['date', 'total_vaccinations','people_fully_vaccinated']][df['location'] == 'Asia']
        df2 = df2[:30]
        df2 = df2.sort_values(by='total_vaccinations', ascending=True)
        data = df2.to_json(df2)
        
        result=df2.to_json(orient='table')
        parsed_result=json.loads(result)
        data = json.dumps(parsed_result['data'])

        return Response(data) 