import argparse
from Bio import Entrez

Entrez.email = "joserodelmar@gmail.com"


print("Introduce los terminos de busqueda")

# Paso de parametros por argumentos
parser = argparse.ArgumentParser(description="Busqueda de terminos en pubmed")
parser.add_argument("-i", "--input",
                    metavar="word of interest",
                    type=str,
                    help="Terminos a buscar",
                    required=True)

args = parser.parse_args()
search1 = args.input


# through handle the terms in "search" will be looked for in pubmed database

print("Ingrese el pais en el que desea buscar")
country = input()
print("Ingrese el año de publicacion que le interesa")
year = input()
print("Ingrese un tema de interes")
topic = input()

search2 = country + "[CNTY] AND " + year + "[PDAT] AND " + topic + "[ALL]"
### through handle the terms in "search" will be looked for in pubmed database

handle = Entrez.esearch(db="pubmed", sort="relevance", term=search2)

record = Entrez.read(handle)  # The results that coincide with the terms in "search" are stored in record
Number = int(record["Count"])  # The number of IDs is stored in Number
IDs = result["IdList"]  # in IDs, the list with the corresponding IDs will be stored
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

# Obtencion del numero de publicaciones referentes al tema de interes de cada autor
for Author in Authors:
    termino = "(" + Author + "[AUTH] AND " + topic + "[ALL])"
    handle = Entrez.esearch(db="pubmed", term=termino)
    record = Entrez.read(handle)
    NumID.append(record["Count"])

handle.close()
