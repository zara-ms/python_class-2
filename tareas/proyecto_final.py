"""
## NAME

	  buscar_autores.py
  
## VERSION

	  [1.0]
  
## AUTHOR

    Jose Rodelmar Ocampo Luna
    Daniela Goretti Castillo Leon
	  Zara Paulina Martinez Sanchez <zaram042001@gmail.com>
  
## DATE

	  03/12/2021
  
 ## DESCRIPTION
 
     Mediante paso de argumentos el usuario puede buscar articulos referentes a algun tema de interes
     los cuales hayan sido publicados en cierto año y pais para asi obtener los primeros autores de hasta
     los 10 primeros articulos mas relevantes. Despues el programa grafica los articulos de los autores encontrados 
     en la fecha determinada, asi como grafica los articulos totales de los autores antes encontrados en relacion con 
     el tema de interes dado por el usuario.
 
## CATEGORY

	  Analysis
    
## EXAMPLES



## GITHUB LINK

	  https://github.com/Rodel-OL/python_class/blob/master/tareas/proyecto_final.py
  
"""

import argparse
from Bio import Entrez
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Entrez.email = "joserodelmar@gmail.com"

# Paso de parametros por argumentos con informacion de cada uno
parser = argparse.ArgumentParser(description="Busqueda de terminos en pubmed")
parser.add_argument("-w", "--word",
                    metavar="word of interest",
                    type=str,
                    help="Terminos a buscar",
                    required=True)

# Search by country and year of publication.
parser.add_argument("-c", "--country",
                    metavar="country of publication",
                    type=str,
                    help="Pais donde se desean buscar las publicaciones",
                    required=True)

parser.add_argument("-y", "--year",
                    metavar="year of publication",
                    type=int,
                    help="Fecha de publicacion del articulo",
                    required=True)

args = parser.parse_args()

search = args.country + "[CNTY] AND " + args.year + "[PDAT] AND (" + args.word + ")"

# Busqueda de la informacion ingresada por el usuario
handle = Entrez.esearch(db="pubmed", sort="relevance", term=search)

record = Entrez.read(handle)  # Obtencion de la informacion de interes acomodada por relevancia
Number = int(record["Count"])  
IDs = record["IdList"]  
handle.close()

# Recortar la lista de IDs en caso de ser necesario
if Number > 10:
    IDs = IDs[0: 10]

# Definir listas vacias a utilizar
Authors = []
NumID = []

# Obtener los primeros autores de los articulos encontrados 
for ID in IDs:
    handle = Entrez.esummary(db="pubmed", id=ID, retmode="xml")
    records = Entrez.parse(handle)
    
    # Guardar los autores en una lista
    for record in records:
        Authors.append(record["AuthorList"][0])

handle.close()

# Funcion nauth para graficar los articulos de autores encontrados en la fecha determinada, solo usa los nombres de autores
def nauth (AUTH):
    AUTHP = sorted(set(AUTH))
    ARTP = [list.count(i) for i in AUTHP]
    data = {"Autores": AUTHP,
            "Articulos": ARTP}
 
    df = pd.DataFrame(data, columns=['Autores', 'Articulos'])

    plt.figure(figsize=(len(AUTHP)*2, len(AUTHP)))
    plots = sns.barplot(x="Autores", y="Articulos", data=df)
    
    plt.title("Autores y numero de articulos en reelvancia en fecha determinada")
    plt.show()


nauth(Authors)

# Obtencion del numero de publicaciones referentes al tema de interes de cada autor
for Author in sorted(set(Authors)):
    termino = "(" + Author + "[AUTH] AND " + topic + "[ALL])"
    handle = Entrez.esearch(db="pubmed", term=termino)
    record = Entrez.read(handle)
    NumID.append(record["Count"])

handle.close()

# Funcion nauth2 para graficar los articulos totales de los autores antes encontrados, obtenidos con ["Count"]
def nauth2 (auth, num):
    data = {"Autores": sorted(set(auth)),
            "Articulos": [int(j) for j in num]}
 
    df = pd.DataFrame(data, columns=['Autores', 'Articulos'])

    plt.figure(figsize=(len(auth)*2, len(auth)))
    plots = sns.barplot(x="Autores", y="Articulos", data=df)
    
    plt.title("Autores y numero de articulos en relevancia totales")
    plt.show()


nauth2(Authors, NumID)
