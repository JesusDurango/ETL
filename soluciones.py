import pandas as pd
import requests
import sqlite3


    
url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
data= pd.read_csv(url, sep=';')
print(data)

registros=[]
cont= 1
def cargar_registro(ciudad,concentraciones, contador):
    registro = {'City':ciudad, 'overall_aqi': concentraciones['overall_aqi']}
    for key in concentraciones:
        if isinstance(concentraciones[key],dict)and 'concentration' in concentraciones[key]:
            registro[key] = concentraciones[key]['concentration']
    registros.append(registro)
    print(f'registro numero{contador}añadido')    

del data['Race']
del data['Count']
del data['Number of Veterans']
data.drop_duplicates(inplace=True)

cities = data['City']
for city in cities :
    api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
    response = requests.get(api_url,headers={'X-Api-Key': 'u7caPVPx2iwbvysrVQYjxw==MHgkEMTJ2IxM5dG2'})
    if response.status_code == requests.codes.ok:
        concentrations = response.json()
        cargar_registro(city,concentrations,cont)
        cont += 1

df_aqis = pd.DataFrame(registros)

connection = sqlite3.connect('calidad_del_aire.db')
df_aqis.to_sql('Concentrations',connection, if_exists='replace', index=False)
data.to_sql('Cities',connection,if_exists='replace',index=False)
connection.close()