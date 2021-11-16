import pandas as pd
import numpy as np
### MULTINDEX
df = pd.DataFrame(np.random.rand(4, 2),
                  index=[['Temperatura', 'Temperatura', 'Fuente carbono', 'Fuente carbono'],
                         ['30', '35', 'glc', 'ace']],
                  columns=['Gen1', 'Gen2'])
print(df)
df_inverso = df = pd.DataFrame(np.random.rand(2, 4),
                  columns=[['Temperatura', 'Temperatura', 'Fuente carbono', 'Fuente carbono'],
                         ['30', '35', 'glc', 'ace']],
                  index=['Gen1', 'Gen2'])

### Constructores
pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])
pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])
pd.MultiIndex.from_product([['a', 'b'], [1, 2]])

### Multindex en index y columnas
expresion = pd.DataFrame(np.random.rand(4, 4),
                  columns=[['Temperatura', 'Temperatura', 'Fuente carbono', 'Fuente carbono'],
                         ['30', '35', 'glc', 'ace']],
                  index=[['E. coli', 'E. coli', 'P. putida', 'P. putida'],
                         ['Gen1', 'Gen2', 'Gen1', 'Gen2']])
print(expresion)
expresion.index.names = ['Organismo', 'Gen']
print(expresion)

# Acceso con loc
print(expresion.loc['E. coli', 'Temperatura'])
print(expresion.loc[('E. coli','Gen1'), 'Temperatura'])

# Acceso con xs
print(expresion.xs("Gen1", level="Gen"))
print(expresion.xs("E. coli", level="Organismo", axis=0))

# Acceso xs y columnas
expresion.columns.names = ['Estres', 'Variacion']
print(expresion)
print(expresion.xs("Temperatura", level="Estrés", axis=1))
print(expresion.xs("glc", level="Variacion", axis=1))

### Groupby : index
df3 = pd.DataFrame({'expresion':np.random.rand(6)},
                 index=['gen1', 'gen2', 'gen3', 'gen1', 'gen2', 'gen3'])
print(df3)
grupos = df3.groupby(level=0)
print(grupos.mean())

### Groupby : columna
df4 = pd.DataFrame({'gen': ['gen1', 'gen2', 'gen3', 'gen1', 'gen2', 'gen3'],
                   'expresion': np.random.rand(6)}, columns=['gen', 'expresion'])
print(df4)
grupos2 = df4.groupby('gen')
print(grupos2.sum())
###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Matplotlib
### import matplotlib as mpl (otra manera de importar matplotlib)
import matplotlib.pyplot as plt

### enfoques>
# Prodedural (se va modificando al anadir funciones)
# Orientado a objeteos (se va modificando usando metodos
# aplicados al objeto axes)

# creamos figura
fig = plt.figure()
# creamos un eje
ax = plt.axes()

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))
plt.show()
ax.set(xlim=(0, 10), ylim=(-2, 2),  #limites
       xlabel="x", ylabel="sen(x)", #etiquetas
       title="grafiquita")       #titulo

# al momento de usar un plt show , matplotlib descarta la figura,
plt.show()
### plt.subplots()
fig, ax = plt.subplots()

plt.plot(x, np.sin(x), "-.")
plt.plot(x, np.cos(x), "o")
plt.show()

### 1:03
### organismos = np.random.choice(['procariotas', 'eucariotas', 'arqueas'], 5, p=[0.5, 0.3, 0.2])
### costo_beneficio['organismos'] = organismos
### costo_beneficio

### https://pandas-profiling.github.io/pandas-profiling/docs/master/rtd/

### https://www.tabnine.com/ este es el link del programa "inteligente" para predecir código
