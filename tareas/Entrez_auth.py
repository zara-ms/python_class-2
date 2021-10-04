'''

NAME
	Entrez_auth.py

VERSION
	[1.0]

AUTHOR
	[Ocampo Luna Jose Rodelmar] <joserodelmar@gmail.com>
	[Other authors]: [Modifications]


DESCRIPTION
	[Acording to input terms, a list with articles IDs will be created]

CATEGORY
	[category of the program: DataBase Analysis]

USAGE
	[Entrez_auth.py][-options/arguments]

ARGUMENTS
	[search]  [Where the input searching terms will be stored]
	[archiv]  [Where the articles IDs corresponding to the search terms will
	            be stored]

INPUT
	[Searching terms that match those used in pubmed search with Entrez]

NOT WORKING INPUT
    [Wrong sintaxis paths, or unexisting fields of search]

OUTPUT
    [archiv list, which stores the searching term's matching articles Ids]

EXAMPLES
    [Program is run
    >Introduce los terminos de busqueda
    input(Amaranta Manrique[AUTH] AND alacranes[Title] OR etica[Title])
    print(archiv)
    >['28350978', '23920463', '22754085', '11401128', '11008361']
    ]

GITHUB
    [https://github.com/Rodel-OL/python_class/blob/master/tareas/Entrez_auth.py]

'''
from Bio import Entrez
Entrez.email = "joserodelmar@gmail.com"
print("Introduce los terminos de busqueda")
### In "search" the users input will be stored
search = str(input())
### through handle the terms in "search" will be looked for in pubmed database
handle = Entrez.esearch(db="pubmed", term=search)
### The results that coincide with the terms in "search" are stored in result
result = Entrez.read(handle)
### in archiv, the list with the corresponding IDs will be stored
archiv = result["IdList"]
### handle must be closed
handle.close()
### To see the IDs that matched the search terms, archiv can be printed
print(archiv)
