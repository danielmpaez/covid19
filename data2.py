# -*- coding: utf-8 -*-

import pandas as pd #importar libreria pandas
import matplotlib.pyplot as plt #importar libreria graficos
import numpy as np
import csv 
import json 
from pymongo import MongoClient

from flask import Flask
from flask import request,render_template

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#from app import app, mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
#from werkzeug import generate_password_hash, check_password_hash

import texttable as tt




#LECTURA DOCUMENTO CSV
covid19 = pd.read_csv('covid.csv')

#CSV A DICCIONARIO DE PYTHON
covid19.to_dict('records')
covid19.head()

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
      
print('\n'* 3)

print("print de arg_casos")
#crear archivo argentina.json,previo archivo csv
Argentina.to_csv (r'dataframe.csv', index = False, header=True)
#with open(Argentina.json, 'w', encoding='utf-8') as jsonf: 
#		jsonf.write(json.dumps(data, indent=4))

arg_casos = pd.read_csv('dataframe.csv')

#CSV A DICCIONARIO DE PYTHON
arg_casos.to_dict('records')
arg_casos.head()
        
print(arg_casos)  




#convertir csv a json

def csv_json(csvFilePath1, jsonFilePath1): 
	
	# CREAMOS DICCIONARIO
	data = {} 
	
	# ABRIMOS Y LEEMOS CSV
	with open(csvFilePath1, encoding='utf-8') as csvf: 
		csvReader = csv.DictReader(csvf) 
		
		
		for rows in csvReader: 
			
		 
			key = rows['deaths'] 
			data[key] = rows 


	with open(jsonFilePath1, 'w', encoding='utf-8') as jsonf: 
		jsonf.write(json.dumps(data, indent=4)) 
		

csvFilePath1 = r'dataframe.csv'
jsonFilePath1 = r'argen_data.json'

csv_json(csvFilePath1, jsonFilePath1)

      
print('\n'* 3)
      
print('\n'* 3)
info=Argentina[['year','month','day','cases','deaths']]
print(info)
print('\n'* 3)
treinta= info[:30]
print(treinta)
print('\n'* 3)

#DIAS CON MAS DE 150 FALLECIODS EN ARGENTINA 
print('\n')
print("------------------------------------------")
print("DIAS CON MAS DE 150 FALLECIDOS")
print("------------------------------------------")
print('\n')
promedio = Argentina.loc[Argentina.deaths>150]
print(promedio)


print("------------------------------------------")
print("ULTIMO MES")
print('\n')
print("------------------------------------------")

#GRAFICO FALLECIDOS ARGENTINA ULTIMOS 30 DIAS
tres = Argentina[:30]
print(tres)
print('\n'* 3)
tres.plot(x="day", y="cases", color="#f44265", lw=3)

#uso de tabla



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
plt.savefig('casos2.jpg')
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
plt.savefig('fallecidos2.jpg')



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
  
# CARGA Y LECTURA DE JSON
with open('covid.json') as file: 
    file_data = json.load(file) 
      
#INSERTAMOS JSON EN DB
if isinstance(file_data, list): 
    Collection.insert_many(file_data)   
else: 
    Collection.insert_one(file_data) 
    
    #------------------------------------------
    
#CREACION DE LA COLECCION ARGENTINA

db = myclient["covid"] 
   
#SELECCION DE COLECCON
 
Collection = db["argentina"] 

# CARGA Y LECTURA DE JSON
with open('argen_data.json') as file: 
    file_data = json.load(file) 
      
#INSERTAMOS JSON EN DB
if isinstance(file_data, list): 
    Collection.insert_many(file_data)   
else: 
    Collection.insert_one(file_data) 






#CRUD






#SERVIDOR  FLASK


app = Flask(__name__)

@app.route("/")
def hello():
         return  render_template('index.html')


@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    print ('Getting RAW Data')
    print (request.get_data())
    print ('Validate JSON Format')
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'

    
@app.route('/index')
def index():
    return  render_template('index.html')

@app.route('/prueba')
def prueba():
    return render_template('index.html', tables=[tres.to_html(classes='data', header="true")]) 


@app.route('/tabla')
def tabla():
    return render_template('tabla.html', tables=[Argentina.to_html(classes='data', header="true")])



@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/paises', methods=['GET'])
def paises():
   with open("dataframe.json") as f:
    data3 = json.load(f)
    return jsonify(data3)

print(data3)
   
     
           
            
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp



if __name__ == "__main__":    
    
    app.run(debug=True) 



'''
COLORES 
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
                                  
