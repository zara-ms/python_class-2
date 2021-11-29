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

search2 = country + "[CNTY] AND " + year + "[PDAT]"
### through handle the terms in "search" will be looked for in pubmed database

handle = Entrez.esearch(db="pubmed", term=search)

# The results that coincide with the terms in "search" are stored in result
result = Entrez.read(handle)

# in archiv, the list with the corresponding IDs will be stored
archiv = result["IdList"]
handle.close()

