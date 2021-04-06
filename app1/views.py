from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404 
from django.shortcuts import render
import os
import pandas as pd
import numpy as np
# Create your views here.

os.chdir(r"C:\Users\suraj\Downloads")
os.getcwd()
os.listdir()
df = pd.read_csv('owid-covid-data.csv', encoding='utf-8', na_values=None, error_bad_lines=False)
df = df.sort_values(by='total_vaccinations', ascending=False)
df.continent = df.continent.str.replace(' ','_')
df.location = df.location.str.replace(' ','_')

def Index(request):
    Country_vacc = {}


    for country in df['location'].unique():    #Create Country_vacc dict for all countery & Total vaccine
        df1 = df[['location', 'date', 'total_vaccinations']][df['location'] == country]
        df1 = int(df1['total_vaccinations'].fillna(0).max())
        Country_vacc[country] = df1
        

    # continent_loc = {}
    # for key, value in Country_vacc.items():
    #     if key in list(df['continent'].unique()[1:]):
    #         continent_loc[key] = value
    #         #del Country_vacc[key]

    conti_name = list(df['continent'].unique()[1:])

    for i in conti_name:  #deletion 
        del Country_vacc[i]
    del Country_vacc["World"]
    
    #Now Creating lable1 = Unique_country names and data1 = Total_Vaccine count for graph Country map
    lable1 = []  #contain Unique_country names
    Data1 = []   #contain Total_Vaccine count

    for i, j in Country_vacc.items():
        lable1.append(i)
        Data1.append(j)
        
    #Now lable2 = Unique_continent location and data2 = Total_Vaccine count for graph continent map
    lable2 = []   #contain Unique_continent location
    Data2 = []    #contain Total_Vaccine count

    # for m, n in continent_loc.items():
    #     lable2.append(m)
    #     Data2.append(n)

    #Sum of Data 
    sum1 = sum(Data1)   #Total in infacted in All over World
    # sum2 = sum(Data2)   #Total in infacted in Continent
    
    #for True condition 
    ShowMap = 'True'  #this is for display using true/false condition display in this section graph model
    
    context1 = {'lable1': lable1, 'Data1': Data1, 'sum1': sum1, 'ShowMap':ShowMap}
    
    return render(request, 'new.html', context1)

def SingleCountry(request):
    Country_vacc = {}

    for country in df['location'].unique():    #Create Country_vacc dict for all countery & Total vaccine
        df1 = df[['location', 'date', 'total_vaccinations']][df['location'] == country]
        df1 = int(df1['total_vaccinations'].fillna(0).max())
        Country_vacc[country] = df1

    conti_name = list(df['continent'].unique()[1:])

    for i in conti_name:  #deletion 
        del Country_vacc[i]
    del Country_vacc["World"]
    
    #Now Creating lable1 = Unique_country names and data1 = Total_Vaccine count for graph Country map
    lable1 = []  #contain Unique_country names
    Data1 = []   #contain Total_Vaccine count

    for i, j in Country_vacc.items():
        lable1.append(i)
        Data1.append(j)
        
    #Now lable2 = Unique_continent location and data2 = Total_Vaccine count for graph continent map
    # lable2 = []   #contain Unique_continent location
    # Data2 = []    #contain Total_Vaccine count

    # for m, n in continent_loc.items():
    #     lable2.append(m)
    #     Data2.append(n)

    #Sum of Data 
    sum1 = sum(Data1)   #Total in infacted in All over World
    # sum2 = sum(Data2)   #Total in infacted in Continent
    
    #Here is Starting point to get the value from Graph buttion and render the data    
    Country = request.POST.get('countryName')
    #selectCountry = "Africa"    ---for verifying by manually insert string value
    df2 = df[['date', 'total_vaccinations','people_fully_vaccinated']][df['location'] == Country]
    df2 = df2[:30]         #Filter 30 days dataset
    df2 = df2.sort_values(by='total_vaccinations', ascending=True)  
    
    lable3 = df2['date'].to_list()  #data-column to list
    temp = df2['total_vaccinations'].fillna(0).to_list()  #data-column to list
    
    #Converting float to int 
    Data3 = []
    for item in temp:
        Data3.append(int(item))
        
    #for True condition 
    ShowMap = 'False'  #this is for display using true/false condition display in this section graph model
    
    context1 = {'lable1': lable1, 'Data1': Data1, 'sum1': sum1, 'lable3': lable3, 'Data3': Data3,'ShowMap':ShowMap}
    
    return render(request, 'new.html', context1)