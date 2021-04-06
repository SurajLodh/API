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
    
        os.chdir(r"C:\Users\suraj\Downloads\practice")
        os.getcwd()
        os.listdir()
        df = pd.read_csv('owid-covid-data.csv', encoding='utf-8', na_values=None, error_bad_lines=False)
        df = df.sort_values(by='total_vaccinations', ascending=False).fillna(0)
        df.continent = df.continent.str.replace(' ','_')
        df.location = df.location.str.replace(' ','_')

        # Country_vacc = {}


        # for country in df['location'].unique():    #Create Country_vacc dict for all countery & Total vaccine
        #     df1 = df[['location', 'date', 'total_vaccinations']][df['location'] == country]
        #     df1 = int(df1['total_vaccinations'].max())
        #     Country_vacc[country] = df1
            

        # continent_loc = {}
        # for key, value in Country_vacc.items():
        #     if key in list(df['continent'].unique()[1:]):
        #         continent_loc[key] = value
                
        conti_name = list(df['continent'].unique()[1:])

        conti = {}
        for i in conti_name:
            df2 = df[df['continent'] == i][['date', 'total_vaccinations','people_fully_vaccinated']]
            df2 = df2[:30]
            df2 = df2.sort_values(by='total_vaccinations', ascending=True)
            result = df2.to_json(orient='table')
            parsed_result = json.loads(result)
            data2 = parsed_result['data']
            conti[i] = data2

        # for i in conti_name:  #deletion 
        #     del Country_vacc[i]
        # del Country_vacc["World"]
        
        # #Now Creating lable1 = Unique_country names and data1 = Total_Vaccine count for graph Country map
        # lable1 = []  #contain Unique_country names
        # Data1 = []   #contain Total_Vaccine count

        # for i, j in Country_vacc.items():
        #     lable1.append(i)
        #     Data1.append(j)
            
        #Now lable2 = Unique_continent location and data2 = Total_Vaccine count for graph continent map
        # lable2 = []   #contain Unique_continent location
        # Data2 = []    #contain Total_Vaccine count

        # for m, n in continent_loc.items():
        #     lable2.append(m)
        #     Data2.append(n)

        #Sum of Data 
        # sum1 = sum(Data1)   #Total in infacted in All over World
        # sum2 = sum(Data2)   #Total in infacted in Continent
        
        #for True condition 
        # ShowMap = 'True'  #this is for display using true/false condition display in this section graph model

        # context1 = {'Country_vacc': Country_vacc, 'continent_loc': continent_loc}
        # context = {'conti':conti,'Country_vacc': Country_vacc}
        return Response(conti) 