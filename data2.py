# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#_*_ coding: utf-8
import pandas as pd #importar libreria pandas
import matplotlib.pyplot as plt #importar libreria graficos
import numpy as np
import csv 
import json 


'''
datos={'Nombre': ['juan','Carlos','juan', 'Pedro'],'Calificaciones':['10',np.nan,'5','10'],'deporte': ['futbol','voley','rugby','tenis'],'asignatura':['Lengua','Matematicas','Ciencias','Dibujo'],'edades':['22','15','17','20']}
df2= pd.DataFrame(datos)
print(df2)
print('\n'* 3)


datos={'Nombre': ['Silvia','Ana','Ernesto', 'Sergio'],'Calificaciones':['10','9','5','10'],'deporte': ['futbol','N/A','rugby','tenis'],'asignatura':['Lengua','Matematicas','Ciencias','Dibujo'],'edades':['22','15','17','20'],'Ciudad':['Lima','Cordoba','Jujuy','Salta'],'Facebook':['si','si','no','si'],'Twitter':['si','no','no','si'],'Instagram':['si','si','si','si']}
df3= pd.DataFrame(datos)
print(df3)
print('\n'* 3)

print("INFO DEL DATAFRAME:  ")
print(df3.info())
print('\n'* 3)


#REEMPLAZAR ELEMENTO
nuevo=pd.DataFrame(df3)
nuevo=nuevo.replace('rugby','pingpong')

print(nuevo)

# ESTADISTICAS
print("ESTADISTICA DATAFRAME")
print(df2.describe())
total =( df2,df3)
print('\n'* 3)


#ELIMINAR POR CONDICION

print("ELIMINANDO QUIENES  ESTUDIAN DIBUJO")

columna= df3[df3['asignatura']!= 'Dibujo']
print(columna)
print('\n'* 3)

#SOLO IMPRIMIR UN DATO ESPECIFICO, EJEMPLO DE QUIEN ESTUDIA MATEMATICAS
print("ESTUDIAN MATEMATICAS")
matematicas =df3[df3['asignatura']=='Matematicas']
print(matematicas)
print('\n'* 3)

print("NO USAN TWUITTER")
noTwitter =df3[df3['Twitter']=='no']
print(noTwitter)
'''
covid19 = pd.read_csv('covid.csv')

covid19.to_dict('records')
covid19.head()
print(covid19)

print("INFO DEL DATAFRAME:  ")
print(covid19.info())
print('\n'* 3)
print(covid19.describe())
print('\n'* 3)


print("INFORME COVID ARGENTINA")
print('\n')
print("------------------------------------------")
Argentina =covid19[covid19['countriesAndTerritories']=='Argentina']
print(Argentina)
print('\n'* 3)



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

print('\n')
print("------------------------------------------")
print("DIAS CON MENOS DE 100 FALLECIDOS")
print("------------------------------------------")
print('\n')
promedio2 = Argentina.loc[Argentina.deaths<500]
print(promedio2)

ax = promedio2.plot.barh(x="day", y="deaths")
plt.show()

#CONVERSION A JSON



# Function to convert a CSV to JSON 
# Takes the file paths as arguments 
def make_json(csvFilePath, jsonFilePath): 
	
	# create a dictionary 
	data = {} 
	
	# Open a csv reader called DictReader 
	with open(csvFilePath, encoding='utf-8') as csvf: 
		csvReader = csv.DictReader(csvf) 
		
		# Convert each row into a dictionary 
		# and add it to data 
		for rows in csvReader: 
			
			# Assuming a column named 'No' to 
			# be the primary key 
			key = rows['deaths'] 
			data[key] = rows 

	# Open a json writer, and use the json.dumps() 
	# function to dump data 
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
		jsonf.write(json.dumps(data, indent=4)) 
		
# Driver Code 

# Decide the two file paths according to your 
# computer system 
csvFilePath = r'covid.csv'
jsonFilePath = r'covid.json'

# Call the make_json function 
make_json(csvFilePath, jsonFilePath)


                                  