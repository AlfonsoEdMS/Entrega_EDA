import pandas as pd 
import numpy as np

# def diccionario(dicc_country):
# global dicc_country
df_1 = pd.read_csv('Total_Energy_Production.csv', sep=',', header = 1, engine='python', index_col=False)
df_1 = df_1.rename(columns= {'API' : 'Country', 'Unnamed: 1' : 'Source' })

'''Creamos un diccionario formado por los países en nuestro DataSet y sus acrónimos'''

lista_0 = []

for m in df_1['Source']:
    lista_0.append(m)
    lista_Paises = lista_0[0::8]

# Una vez sacamos una lista de totdos los países eliminamos la filas con NAn
df_1 = df_1.dropna(axis=0, thresh=39)
df_1.head(10)

#Lista de Países
# lista_Paises

lista_1 = []
lista_2 = []

for n in df_1['Country']:
    string = n.split('-')
    lista_1.append(string)
# print(lista_1)
for m in lista_1:
    elemento = m[2]
    lista_2.append(elemento)
# print(lista_2)


df = np.array(lista_2) # Lo convertimos a array 
df = pd.DataFrame(df) # Lo convertimos a array
df.rename(columns= {0:'col'}, inplace=True)
df['col'].unique()
# Hacemos un diccionario donde tengamos todos los píses y sus acrónimos.
dicc_country = dict(zip(lista_Paises, df['col'].unique()))
dicc_country_1 = dict(zip(df['col'].unique(),lista_Paises))



# def list_todos(dicc_country):
# global ltW
ltW = []
for x in dicc_country.keys():
    ltW.append(x)

# def list_todos(dicc_country):
# global cdW
cdW = []
for y in dicc_country.values():
    cdW.append(y)

