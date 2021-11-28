from Bio import Entrez
Entrez.email = "joserodelmar@gmail.com"
print("Introduce los terminos de busqueda")
search = str(input())
### through handle the terms in "search" will be looked for in pubmed database
handle = Entrez.esearch(db="pubmed", term=search)
### The results that coincide with the terms in "search" are stored in result
result = Entrez.read(handle)
### in archiv, the list with the corresponding IDs will be stored
archiv = result["IdList"]
handle.close()
