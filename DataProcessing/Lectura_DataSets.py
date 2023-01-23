import pandas as pd 
import numpy as np
from Listas import North_America, Cen_Sth_America, Europe, Eurasia, Africa, Middle_East, Asia_Oceania, lst_SRC_C, lst_SRC_P
from Variables import dicc_country, ltW, cdW
pd.set_option('display.max_rows', 45)

# ------ dfP -------

# Primary Energy ((Production Btu))

df_1 = pd.read_csv('Total_Energy_Production.csv', sep=',', header = 1, engine='python', index_col=False)
df_1 = df_1.rename(columns= {'API' : 'Code',
'Unnamed: 1' : 'Source' })

'''Limpiamos nuestras columnas y nos quedamos únicamente con los países de nuestro DataSet y sus acrónimos'''

# Una vez sacamos una lista de totdos los países eliminamos la filas con NAn
df_1 = df_1.dropna(axis=0, thresh=39)

#Lista de Países
# lista_'Code'

lista_1 = []
lista_2 = []

for n in df_1['Code']:
    string = n.split('-')
    lista_1.append(string)
# print(lista_1)
for m in lista_1:
    elemento = m[2]
    lista_2.append(elemento)
# print(lista_2)
#Modificamos la columna 'Code'
df_1['Code'] = lista_2

'''Modificamos la columna 'Source'; Recordar que las unidades son (quad Btu)'''

# lst_SRC_P = ['Production', 'Coal', 'Natural gas', 'Petroleum and other liquids', 'Nuclear, renewables, and other', 'Nuclear', 'Renewables']
arr = df_1['Source'].unique()
lst_SRC_old = arr.tolist()
src = zip(lst_SRC_P, lst_SRC_old)
source = list(src)

for list in source:
    df_1.replace(list[1], 
           list[0], 
           inplace=True)

# df_1['Source'].unique()

#to numeric
# dfs.loc[:,'1980':'2019'] = dfs.loc[:,'1980':'2019'].apply(pd.to_numeric())
for col in df_1.loc[:,'1980':'2019']:
    df_1[col] = pd.to_numeric(df_1[col], errors ='coerce')

'''df_1 es la versión extendidad de dfP'''

df_1.replace(0.0, np.nan, inplace=True)
df_1 = df_1.dropna(thresh=4).reset_index(drop=True)
df_1 = df_1.fillna(0)

'''Creamos dfP que es el DataSet con el que vamos a trabajar (desde 1997 hasta 2019)'''

dfP = df_1.drop(df_1.loc[:, '1980':'1996'], axis=1)
dfP.replace(0.0, np.nan, inplace=True)
dfP = dfP.dropna(thresh=4).reset_index(drop=True)
dfP = dfP.fillna(0)

# ------ dfP -------

# ------ dfC -------

# Consumo 

df_2 = pd.read_csv('Total_Energy_Consumption.csv', sep=',', header = 1, engine='python', index_col=False)
df_2 = df_2.rename(columns= {'API' : 'Code',
'Unnamed: 1' : 'Source'})

'''Limpiamos nuestras columnas y nos quedamos únicamente con los países de nuestro DataSet y sus acrónimos'''
# len(df_2['Source']), Resp: 1848
# len(df_2['Source']) / 8 , Resp: 231
df_2['Source'] = ['Country', 'Consumption', 'Coal', 'Natural gas', 'Petroleum and other liquids', 'Nuclear, renewables, and other', 'Nuclear', 'Renewables'] * 231

#def clean_data():
# Una vez sacamos una lista de totdos los países eliminamos la filas con NAn
df_2 = df_2.dropna(axis=0, thresh=39)

#Lista de Países
# lista_Paises

lista_1 = []
lista_2 = []

for n in df_2['Code']:
    string = n.split('-')
    lista_1.append(string)
# print(lista_1)
for m in lista_1:
    elemento = m[2]
    lista_2.append(elemento)
# print(lista_2)
#Modificamos la columna 'Code'
df_2['Code'] = lista_2

'''Modificamos la columna 'Source'; Recordar que las unidades son (quad Btu); 
Al ponerlo todo en el mismo Script me saltaba el siguiente error: 'Tuple error...' 
Tuve que que sustituir este paso por uno más arriba y con una lógica más sencilla'''

# arr = df_2['Source'].unique()
# lst_SRC_old = arr.tolist()
# src = zip(lst_SRC_C, lst_SRC_old)
# # source = list(src)

# for list in source:
#     df_2.replace(list[1], 
#            list[0], 
#            inplace=True)

df_2['Source'].unique = ['Consumption', 'Coal', 'Natural gas', 'Petroleum and other liquids',
       'Nuclear, renewables, and other', 'Nuclear', 'Renewables']

#to numeric
# dfs.loc[:,'1980':'2019'] = dfs.loc[:,'1980':'2019'].apply(pd.to_numeric())
for col in df_2.loc[:,'1980':'2019']:
    df_2[col] = pd.to_numeric(df_2[col], errors ='coerce')

'''df_1 es la versión extendidad de dfP'''

df_2.replace(0.0, np.nan, inplace=True)
df_2 = df_2.dropna(thresh=4).reset_index(drop=True)
df_2 = df_2.fillna(0)

'''Creamos dfC que es el DataSet con el que vamos a trabajar (desde 1997 hasta 2019)'''

dfC = df_2.drop(df_2.loc[:, '1980':'1996'], axis=1)
dfC.replace(0.0, np.nan, inplace=True)
dfC = dfC.dropna(thresh=4).reset_index(drop=True)
dfC = dfC.fillna(0)

# ------ dfC -------

# ---- dfNP ------ 

# Nivel poblacional Mundial -> Population (Mperson)

df_3 = pd.read_csv('Population.csv', sep=',', header = 1, engine='python', index_col=False)
df_3 = df_3.rename(columns= {'API' : 'Code',
'Unnamed: 1' : 'Country'})

# Una vez sacamos una lista de totdos los países eliminamos la filas con NAn
df_3 = df_3.dropna(axis=0, thresh=39)
# df_2.head(10)

#Lista de Países
# lista_Paises

lista_1 = []
lista_2 = []

for n in df_3['Code']:
    string = n.split('-')
    lista_1.append(string)
# print(lista_1)
for m in lista_1:
    elemento = m[2]
    lista_2.append(elemento)
# print(lista_2)

df_3['Code'] = lista_2

#to numeric
# dfs.loc[:,'1980':'2019'] = dfs.loc[:,'1980':'2019'].apply(pd.to_numeric())
for col in df_3.loc[:,'1980':'2019']:
    df_3[col] = pd.to_numeric(df_3[col], errors ='coerce')

df_3 = df_3.fillna(method="bfill", axis=1)
df_3 = df_3.fillna(method="ffill", axis=1) 
dfNP = df_3.drop(df_3.loc[:, '1980':'1996'], axis=1)

for col in dfNP.loc[:,'1997':'2020']:
    dfNP[col] = pd.to_numeric(dfNP[col], errors ='coerce')

# ---- dfNP ------ 

# ----- dfEI -------

# Energy Intensity; Population (MMBtu/person)

'''Información incompleta'''
# df_4 = df_2 = pd.read_csv('KWh_persona.csv', sep=',', header = 2, engine='python', index_col=False)
# df_4.head()
'''Otro tipo de formato'''
# df_EI = pd.read_csv('Energy_Intensity.csv', sep=',', header = 1, engine='python', index_col=False)
# df_EI.T.head(10)

dfEI = pd.read_csv('Energy_Intensity_2.csv', sep=',', header = 1, engine='python', index_col=False)
dfEI = dfEI.rename(columns= {'API' : 'Code',
'Unnamed: 1' : 'Country'})

'''Limpiamos nuestras columnas y nos quedamos únicamente con los países de nuestro DataSet y sus acrónimos'''

#def clean_data():
# Una vez sacamos una lista de totdos los países eliminamos la filas con NAn
dfEI = dfEI.dropna(axis=0, thresh=41)

#Lista de Países
# lista_Paises

lista_1 = []
lista_2 = []

for n in dfEI['Code']:
    string = n.split('-')
    lista_1.append(string)
# print(lista_1)
for m in lista_1:
    elemento = m[2]
    lista_2.append(elemento)
# print(lista_2)
#Modificamos la columna 'Code'
dfEI['Code'] = lista_2

dfEI = dfEI.drop(dfEI.index[1::2])
dfEI = dfEI.drop(['Country'], axis = 1).reset_index(drop=True)

#to numeric
# dfs.loc[:,'1980':'2019'] = dfs.loc[:,'1980':'2019'].apply(pd.to_numeric())
for col in dfEI.loc[:,'1980':'2019']:
    dfEI[col] = pd.to_numeric(dfEI[col], errors ='coerce')

'''df_4 es la versión extendidad de dfEI'''
df_4 = dfEI.copy()
df_4.replace(0.0, np.nan, inplace=True)
df_4 = df_4.dropna(thresh=4).reset_index(drop=True)
df_4 = df_4.fillna(0)

'''Creamos dfEI que es el DataSet con el que vamos a trabajar (desde 1997 hasta 2019)'''

dfEI = dfEI.drop(dfEI.loc[:, '1980':'1996'], axis=1)
dfEI.replace(0.0, np.nan, inplace=True)
dfEI = dfEI.dropna(thresh=4).reset_index(drop=True)
dfEI = dfEI.fillna(0)

# ----- dfEI -------

# ---- dfGDP -------

# Gross Domestic Product (Billion$ PPP) 

'''Importamos siempre todo lo necesario para nuestro exploratorio de datos'''

df_GDP = pd.read_csv('Gross_Domestic_Product.csv', sep=',', header = 1, engine='python', index_col=False)

'''Modificamos el nombre de nuestras columnas y 
eliminamo aquellas filas que presenten en su mayoría NaNs'''

df_GDP = df_GDP.rename(columns= {'API' : 'Code',
'Unnamed: 1' : 'Country'})
# df_GDP = df_GDP.dropna(thresh=42)
df_GDP = df_GDP.dropna(subset=['Code'])

'''Añadimos la columna de Country de forma que sea 
identica a los demás DataFrames'''

lista_1 = []
lista_2 = []

for n in df_GDP['Code']:
    string = n.split('-')
    lista_1.append(string)
# print(lista_1)
for m in lista_1:
    elemento = m[2]
    lista_2.append(elemento)
# print(lista_2)

df_GDP['Code'] = lista_2

'''Pasamos a numérico todas aquellas columnas
 con las que vamos a operar'''

for col in df_GDP.loc[:,'1980':'2020']:
    df_GDP[col] = pd.to_numeric(df_GDP[col], errors ='coerce')

'''Finalmente nos quedamos únicamente con Dos DataSets 
1) Más completo pero con Nan
2) Uno completamente limpio para hacer gráficos'''

df_GDP = df_GDP.dropna(thresh=3).reset_index(drop=True)
# dfGDP = df_GDP.dropna(axis= 1).reset_index(drop=True) 
dfGDP = df_GDP.drop(df_GDP.loc[:, '1980':'1996'], axis=1)
dfGDP = dfGDP.drop('Country', axis=1)

for col in dfGDP.loc[:,'1997':'2020']:
    dfGDP[col] = pd.to_numeric(df_GDP[col], errors ='coerce')

dfGDP = dfGDP.fillna(method="bfill", axis=1)
dfGDP = dfGDP.fillna(method="ffill", axis=1)

# Producto Interior Bruto per Cápita
df_6 = pd.read_csv('GDP_per_Capita.csv', sep=',', header = 2, engine='python')

'''Modificamos el nombre de nuestras columnas y 
eliminamo aquellas filas que presenten en su mayoría NaNs'''

df_6 = df_6.rename(columns= {'Country Name' : 'Country',
 'Country Code' : 'Code' })
df_6 = df_6[['Country','Code','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']]
# len(cdW) o len(dfGDP['Code'])
df_6 = df_6[df_6['Code'].isin(dfGDP['Code'])]
dfGDPC = df_6.fillna(method="bfill", axis=1)
dfGDPC = dfGDPC.fillna(method="ffill", axis=1)

for col in dfGDPC.loc[:,'1997':'2020']:
    dfGDPC[col] = pd.to_numeric(dfGDPC[col], errors ='coerce')


# ---- dfGDP/dfGDPC -------

# ----- dfAE ------

# Access to electricity (% of population)

df_E = pd.read_csv('WDIData.csv', sep=',', engine='python', index_col=False)

''' Filtramos nuestro DataSet'''

# df_P1 = df_E[df_E['Country Name'].isin(ltW)]
# df_P1['Country Name'].nunique()
df_E = df_E[df_E['Country Code'].isin(cdW)]

'''Escogemos únicamente el dato que nos interesa y
 entre el espacio temporal que estudiamos'''

df_AE = df_E[df_E['Indicator Name'] == 'Access to electricity (% of population)']
df_AE = df_AE.drop(df_AE.loc[:,'1960':'1979'], axis=1)

'''Limpiamos por encima nuestro DataSet para que quede 
equivalente a loos demás'''

df_AE = df_AE.drop(df_AE.loc[:,'Indicator Name':'Indicator Code'], axis=1)
df_AE.reset_index(drop=True, inplace=True)
df_AE.rename(columns={'Country Name': 'Country', 'Country Code': 'Code'}, inplace=True)

'''Nos deshacemos de las olumnas totalmente vacías y
creamos dos DataSets por separado
1) Uno más completo pero con Nan
2) Otro que abarco un período menor pero completamente limpio de Nan'''

df_AE = df_AE.dropna(how='all', axis=1)
df_AE = df_AE.dropna(thresh=3, axis=0).reset_index(drop=True)
dfAE = df_AE.dropna(axis= 1).reset_index(drop=True)

'''
Hay que saber interpretar el resultado:
- Si el coeficiente sale 0 , seguramente no haya existido una evolución entre el periodo estudiado
- Si el coeficiente inf, solo existe uno de los pparamatros necesarios para lo operación o el coeficiente es negativo
- Si el coeficiente indica "float64%" no existe datos para resolver la operación
'''

#He calculado el coeficiente de progreso desde el año 1998 a 2018

def relative_change(df, anio_M, anio_m):
    locura = []
    for pais in df['Country'].unique():
        n1 = df[df['Country'] == pais][anio_M] - df[df['Country'] == pais][anio_m]
        n2 = df[df['Country'] == pais][anio_m]
        n3 = round(((n1/n2) * 100) , 3)
        dato = str(n3)
        locura.append(dato)
    # return locura
    
    lst_182= []
    for num in locura:
        txt = num.split(' ')
        # print(txt)
        txt2 = txt[4]
        # print(txt2)
        txt3 = txt2.split('\ndtype:')
        # print(txt3)
        txt4 = txt3[0]
        # if txt4 == 'float64':
        #    txt4 = txtX[X]
        lst_182.append(txt4)

    return pd.Series(lst_182)

ds1 = relative_change(dfAE,'2019', '2011')
 
'''Estos países tienen una desarrollo negativo'''

ds1[36] = '-6.459'
ds1[107] = '-14.33'
ds1[135] = '-0.894'
ds1[157]= '-0.2'
ds1[176]= '-2.483'

# pd.to_numeric(ds1) # AE['Relative Change (%)'] = ds1
dfAE['Relative Change (%)'] = pd.to_numeric(ds1, errors ='coerce')

# ----- dfAE ------