import argparse
from Bio import Entrez
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Entrez.email = "joserodelmar@gmail.com"

# Paso de parametros por argumentos
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

#print("Ingrese el pais en el que desea buscar")
#country = input()
#print("Ingrese el año de publicacion que le interesa")
#year = input()
#print("Ingrese un tema de interes")
#topic = input()

### through handle the terms in "search" will be looked for in pubmed database

handle = Entrez.esearch(db="pubmed", sort="relevance", term=search)

record = Entrez.read(handle)  # The results that coincide with the terms in "search" are stored in record
Number = int(record["Count"])  # The number of IDs is stored in Number
IDs = record["IdList"]  # in IDs, the list with the corresponding IDs will be stored
handle.close()

# Recortar la lista de IDs en caso de ser necesario
if Number > 10:
    IDs = IDs[0: 10]

# Definir listas vacias
Authors = []
NumID = []

# Obtener los primeros autores de los papers mas relevantes
for ID in IDs:
    handle = Entrez.esummary(db="pubmed", id=ID, retmode="xml")
    records = Entrez.parse(handle)
    for record in records:
        Authors.append(record["AuthorList"][0])

handle.close()

def nauth (AUTH):
    AUTHP = sorted(set(AUTH))
    ARTP = [list.count(i) for i in AUTHP]
    data = {"Autores": AUTHP,
            "Articulos": ARTP}
 
    df = pd.DataFrame(data, columns=['Autores', 'Articulos'])

    plt.figure(figsize=(len(AUTHP)*2, len(AUTHP)))
    plots = sns.barplot(x="Autores", y="Articulos", data=df)
    
    plt.title("Autores y numero de articulos en reelvancia")
    plt.show()


nauth(Authors)

# Obtencion del numero de publicaciones referentes al tema de interes de cada autor
for Author in Authors:
    termino = "(" + Author + "[AUTH] AND " + topic + "[ALL])"
    handle = Entrez.esearch(db="pubmed", term=termino)
    record = Entrez.read(handle)
    NumID.append(record["Count"])

handle.close()
