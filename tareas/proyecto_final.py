from Bio import Entrez

Entrez.email = "joserodelmar@gmail.com"

print("Ingrese el pais en el que desea buscar")
country = input()
print("Ingrese el año de publicacion que le interesa")
year = input()

search = country + "[CNTY] AND " + year + "[PDAT]"
### through handle the terms in "search" will be looked for in pubmed database
handle = Entrez.esearch(db="pubmed", term=search)
### The results that coincide with the terms in "search" are stored in result
result = Entrez.read(handle)
### in archiv, the list with the corresponding IDs will be stored
archiv = result["IdList"]
handle.close()
