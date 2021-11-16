### PANDAS CON DATA.FRAME ###
###Crear Data.frame desde cero
import pandas as pd
import numpy as np

pd_DF = pd.DataFrame(np.random.rand(3,2),
                     columns=['columna_1', 'clumna_2'],
                     index=['a','b','c'])
print(pd_DF)

### Ejercicio 1 con data.frames

produccion = pd.Series([5, 11, 4, 7, 2],
                        index=['gen1', 'gen2', 'gen3', 'gen4', 'gen5'],
                        name='produccion')
costos = pd.Series([ 5, 4.3, 7, 3.5],
                  index=['gen1', 'gen2', 'gen3', 'gen5'],
                  name='costos')
costo_beneficio = pd.DataFrame({'costos': costos,
                       'produccion': produccion})
print(costo_beneficio)

### Que se puede ver en cuando hay orden de data.frame
print(costo_beneficio.index)
print(costo_beneficio.values)
print(costo_beneficio.keys)
print(costo_beneficio.columns)

### Acceso con loc
### loc es para acceder por el nombre del gen (labels),
# iloc es para indies numericos
print(costo_beneficio.nombre_columna)
# costo_beneficio.loc[idx, columna] ### nombre del indice y columna
print(costo_beneficio.costos)
print(costo_beneficio.loc['gen1','costos'])
### Otras formas de accesar
#['gen1'::2,'costos']
#['gen3':,'costos']
#['gen2':'gen4','costos']
### Acceso especifico
genes_interes = ['gen1', 'gen5']
print(costo_beneficio.loc[genes_interes,'costos'])

### Solo una columna
print(costo_beneficio.costos) # manera mas rapida
print(costo_beneficio.loc[:,'costos']) #Si no necesitas un subset

### iloc
costo_beneficio.head(1)
#costo_beneficio.iloc[idx, columna]
print(costo_beneficio.head(1))
print(costo_beneficio.iloc[0:2, 1])
print(costo_beneficio.iloc[::-2, 1])
print(costo_beneficio.iloc[3:,:])
#valores especificos
idxs = [0,4]
print(costo_beneficio.iloc[idxs, 1])

### iloc y loc
print(costo_beneficio.iloc[[0,2,4],
                           costo_beneficio.columns.get_loc('costos')])
print(costo_beneficio.loc[costo_beneficio.index[[0, 2, 4]], 'costos'])

### Operaciones
print(costo_beneficio.costos + costo_beneficio.produccion)
#Agregar ademas una columna
costo_beneficio['doble'] = costo_beneficio.costos*2
print(costo_beneficio)

### Ejercicio 1
# costos unitarios
costo_beneficio['unitario'] = costo_beneficio.costos/costo_beneficio.produccion
# indices valores maximos
# costo_beneficio.unitario.max() # una sola columna
costo_beneficio.unitario.idxmax()
costo_beneficio.idxmax()
# especificando eje
costo_beneficio.idxmax(axis=1)

### Ejercicio 2
produccion_30 = pd.Series([5, 11, 4, 7, 2],
                        index=['gen1', 'gen2', 'gen3', 'gen4', 'gen5'],
                        name='produccion')
produccion_35 = pd.Series([3, 7, 9, 4, 6],
                        index=['gen1', 'gen2', 'gen3', 'gen4', 'gen5'],
                        name='produccion')
costos2 = pd.Series([ 3.5, 5, 7, 4.3],
                  index=['gen1', 'gen2', 'gen3', 'gen5'],
                  name='costos')
costo_beneficio2 = pd.DataFrame({'costos': costos2,
                       'produccion 30°': produccion_30,
                        'produccion 35°': produccion_35})
print(costo_beneficio2)
# costo unitario
# print([produccion_30, produccion_35] / costos2)
columnas_interes = costo_beneficio2.loc[:,'produccion_30°','produccion_35°']
producciones = costo_beneficio2.loc[:, columnas_interes]
# division
costos_unitarios = producciones.div(costo_beneficio2.costos, axis=0)
# renombrar
costos_unitarios.rename(columns = {'produccion 30°':'new_col1'})
# pero aqui no se quedan los cambios...
costos_unitarios.rename(columns = {'produccion 30°':'costo unitario 30°',
                                   'produccion 35°':'costo unitario 35°'},
                                  inplace=True)
# ahora si se quedan los cambios
# juntando los data.frames
pd.concat([costo_beneficio ,costos_unitarios],axis=1)

### Acceso con booleanos
print(costo_beneficio2.isin([5]))
organismos = np.random.choice(['procariotas', 'eucariotas', 'arqueas'], 5, p=[0.5, 0.3, 0.2])
costo_beneficio2['organismos'] = organismos
print(costo_beneficio2)
print(costo_beneficio.organismos.isin(['procariotas', 'arqueas']))