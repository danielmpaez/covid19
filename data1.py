
#_*_ coding: utf-8
import pandas as pd #importar libreria pandas
import matplotlib.pyplot as plt #importar libreria graficos
import numpy as np

#creamos Dataframe vacio
df = pd.read_csv("./data.csv")
df_filtrado = df.dropna()
df_filtrado.head(5)

#print(df)

info = df
cuadro =pd.DataFrame(info)
#print(cuadro)

datos={'Nombre': ['juan','Carlos','juan', 'Pedro'],'Calificaciones':['10',np.nan,'5','10'],'deporte': ['futbol','voley','rugby','tenis'],'asignatura':['Lengua','Matematicas','Ciencias','Dibujo'],'edades':['22','15','17','20']}
df2= pd.DataFrame(datos)
print(df2)
print('\n'* 3)


datos={'Nombre': ['Silvia','Ana','Ernesto', 'N/A'],'Calificaciones':['10','9','5','10'],'deporte': ['futbol','N/A','rugby','tenis'],'asignatura':['Lengua','Matematicas','Ciencias','Dibujo'],'edades':['22','15','17','20']}
df3= pd.DataFrame(datos)
print(df3)
print('\n'* 3)

total =( df2,df3)
print(total)