import requests
import pandas as pd
import json
import openmeteo_requests 
import googlemaps
from datetime import datetime


#This function retrieves data from Open Meteo.com and saves data in json format
def fetch_weather_data():
    
    url = "https://api.open-meteo.com/v1/forecast?latitude=45.0705,41.8919,39.2305,43.7085,43.7792&longitude=7.6868,12.5113,9.1192,10.4036,11.2463&hourly=temperature_2m"
    
    r = requests.get(url)

    return r.json()


def saveDatasToJson(file):
        
    dataCities = []
        
    dataCities.append(file)
    content = json.dumps(dataCities, indent=4)
    
    print(file[0]["latitude"])
    
    with open("data/citiesdatas.json", "w") as filej:
        filej.write(content)
    
    
def saveDataToCsv(file):
    
    cities = ["Torino", "Roma", "Cagliari", "Pisa", "Firenze"]
    
    df = pd.concat([
        pd.DataFrame({
            "city": cities[i],
            "time": pd.to_datetime(file[i]["hourly"]["time"]),
            "temperature": file[i]["hourly"]["temperature_2m"]
        })
        for i in range(len(cities))
    ])
    
    df.to_csv("data/cities_data.csv", index=False) 
    print("Dati salvati in un dataframe e sul csv")   

if __name__ == "__main__":
    datas = fetch_weather_data()
    
    #saveDatasToJson(datas)
        
    saveDataToCsv(datas)
    
    

