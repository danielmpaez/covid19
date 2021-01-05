# -*- coding: utf-8 -*-

import pandas as pd #importar libreria pandas
import matplotlib.pyplot as plt #importar libreria graficos
import numpy as np
import csv 
import json 
from pymongo import MongoClient


#LECTURA DOCUMENTO CSV
covid19 = pd.read_csv('covid.csv')

covid19.to_dict('records')
covid19.head()
print(covid19)
print("------------------------------------------")
print("------------------------------------------")
print("FUENTE: 'PORTAL EUROPEO DE DATOS' ")
print("https://www.europeandataportal.eu/es")
print("------------------------------------------")
print("------------------------------------------")

#PRESENTACION DEL DOCUMENTO COMO DATAFRAME
print("INFO DEL DATAFRAME:  ")
print(covid19.info())
print('\n'* 3)
print(covid19.describe())
print('\n'* 3)


#INFORME SOLO DATOS ARGENTINA
print("INFORME COVID ARGENTINA")
print('\n')
print("------------------------------------------")
Argentina =covid19[covid19['countriesAndTerritories']=='Argentina']
print(Argentina)
print('\n'* 3)
info=Argentina[['year','month','day','cases','deaths']]
print(info)
print('\n'* 3)
treinta= info[:30]
print(treinta)
print('\n'* 3)
#UNFO FALLECIDOS EN ARGENTINA
print("FALLECIDOS EN ARGENTINA")
FALLECIDOS= Argentina.loc[:'deaths']
print(FALLECIDOS)
#ax = FALLECIDOS.plot.barh(x="deaths", y="day")
#FALLECIDOS.plot.hist(x="day", y="cases",ax=ax, color="C2")
#plt.show()

print('\n')
print("------------------------------------------")
print("DIAS CON MAS DE 150 FALLECIDOS")
print("------------------------------------------")
print('\n')
promedio = Argentina.loc[Argentina.deaths>150]
print(promedio)


print("------------------------------------------")
print("TRES PRIMEROS")
print('\n')
print("------------------------------------------")

#GRAFICO FALLECIDOS ARGENTINA ULTIMOS 30 DIAS
tres = Argentina[:30]
print(tres)
print('\n'* 3)
tres.plot(x="day", y="cases", color="#f44265", lw=3)


plt.xlabel("CASOS", 
           family='sans-serif', 
           color='r', 
           weight='normal', 
           size = 16,
           labelpad = 6)
plt.ylabel('DIAS',
           family='fantasy', 
           color='g', 
           weight='normal', 
           size = 12,
           labelpad = 6)
           
plt.title("CONTAGIADOS ULTIMOS 30 DIAS EN ARGENTINA ",
          position=( 0.5,0.9),
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 10,
                    })
tres.plot(x="day", y="deaths", color="#f44265", lw=3)
plt.text(15, 4500, "Hecho en Python y Pandas",fontsize=6,color='r',rotation=270)

#graf = tres.plot(x="day", z="cases")



plt.xlabel("FALLECIDOS", 
           family='sans-serif', 
           color='r', 
           weight='normal', 
           size = 16,
           labelpad = 6)
plt.ylabel('DIAS',
           family='fantasy', 
           color='g', 
           weight='normal', 
           size = 12,
           labelpad = 6)
           
plt.title("FALLECIDOS ULTIMOS 30 DIAS EN ARGENTINA ",
          position=( 0.5,0.9),
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 10,
                    })
plt.text(20, 60, "Hecho en Python y Pandas",fontsize=6,color='r',rotation=270)




plt.legend()
plt.show()



# DIAS CON MAS Y MENOS CASOS Y FALLECIDOS


idxs = Argentina.groupby(["cases"])["day"].agg(["idxmin", "idxmax"])
maximos = Argentina.loc[idxs["idxmax"]]
minimos = Argentina.loc[idxs["idxmin"]]
print(".................................................")
print("  *** MAXIMOS ***")
print("---------------------------------------------------")
print(maximos)
print('\n' * 3)
print(".................................................")
print("  *** MINIMOS ***")
print("---------------------------------------------------")
print(minimos)


print('\n')
print('\n')
print("------------------------------------------")
print("DIAS CON MENOS DE 100 FALLECIDOS")
print("------------------------------------------")
print('\n')
promedio2 = Argentina.loc[Argentina.deaths<500]
print(promedio2)
'''
ax = promedio2.plot.barh(x="day", y="deaths")
plt.show()
'''
#CONVERSION A JSON




# FUNCION PARA CONVERTIR CSV  A JSON
def make_json(csvFilePath, jsonFilePath): 
	
	# CREAMOS DICCIONARIO
	data = {} 
	
	# ABRIMOS Y LEEMOS CSV
	with open(csvFilePath, encoding='utf-8') as csvf: 
		csvReader = csv.DictReader(csvf) 
		
		
		for rows in csvReader: 
			
		 
			key = rows['deaths'] 
			data[key] = rows 


	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
		jsonf.write(json.dumps(data, indent=4)) 
		

csvFilePath = r'covid.csv'
jsonFilePath = r'covid.json'

make_json(csvFilePath, jsonFilePath)


#EXPORTANDO DATOS A BASE DE DATOS MONGO DB


  
  
  
# c¿CONEXION A LA BASE DE MONGO DB 
myclient = MongoClient("mongodb://localhost:27017/")  
   
# SELECCION DE BASE DE DATOS
db = myclient["covid"] 
   
#SELECCION DE COLECCON
 
Collection = db["data"] 
  
# LCARGA Y LECTURA DE JSON
with open('covid.json') as file: 
    file_data = json.load(file) 
      
#INSERTAMOS JSON EN DB
if isinstance(file_data, list): 
    Collection.insert_many(file_data)   
else: 
    Collection.insert_one(file_data) 

''' COLORES 
Alias	Color
b	Azul
g	verde
r	Rojo
c	cyan
m	magenta
y	amarillo
k	negro
w	blanco

TIPOS DE LETRA

[ 'serif' | 'sans-serif' | 'cursive' | 'fantasy' | 'monospace' ]
'''
                                  
