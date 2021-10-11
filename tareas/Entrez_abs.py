'''

NAME
	Entrez_abs.py

VERSION
	[1.0]

AUTHOR
	[Ocampo Luna Jose Rodelmar] <joserodelmar@gmail.com>
	[Other authors]: [Modifications]


DESCRIPTION
	[Program gets IDs of articles that match a search through Entrez, as well as
	their abstracts, and the IDs of articles that cite them]

CATEGORY
	[category of the program: Database Analysis]

USAGE
	[Entrez_abs.py][-options/arguments]

ARGUMENTS
	[archiv]  [Where matching IDs are saved]
	[ABSTRACTS]  [Where matching article's abstracts are saved]
	[ABS2]  [Where IDs of matching articles with abstract are stored]
	[CITE]  [Where citation article's IDs are stored]

INPUT
	[Searching terms that match those used in pubmed search with Entrez]

NOT WORKING INPUT
    [Wrong sintaxis paths, or unexisting fields of search. For latter loops, if articles
    lack an abstract or sources that cite them, the user will be notified, but those won't
    affect the continuity of the program]

OUTPUT
    [files: Uso_Entrez.txt (stores search matching IDs)
            Uso_Entrez2.txt (stores abstracts of matching IDs)
            Uso_Entrez3.txt (stores citing ids of files with existing abstracts)
    on the run : IDs of search matching articles
                 Articles with no abstract
                 If an article is cited and how many time, or if it is not]

EXAMPLES
    [Program is run
    >Introduce los terminos de busqueda
    input(Amaranta Manrique[AUTH] AND alacranes[Title] OR etica[Title])
    >['28350978', '23920463', '22754085', '11401128', '11008361']
    >Articulo con ID [ 28350978 ] No posee 'abstract' extraible
    >articulo 23920463 No es citado por el momento
    >Hay 1 articulos que citan a  22754085
    >Hay 43 articulos que citan a  11401128
    >articulo 11008361 No es citado por el momento]

GITHUB
    [https://github.com/Rodel-OL/python_class/blob/master/tareas/Entrez_abs.py]

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
handle.close()
### To see the IDs that matched the search terms, archiv can be printed
print(archiv)

### A file is created that contains the IDs of matching articles
Lista_Articulos = open("Uso_Entrez.txt", "w")
Lista_Articulos.write(str(archiv))
Lista_Articulos.close()

### list ABSTRACTS will save the article's abstract extracted in the next loop
ABSTRACTS = []
### ABS2 will save the articles with abstract to extract the articles that cite them
ABS2 = []
### CITE will save the articles that reference the articles with abstracts
CITE = []

for ids in archiv:
    ### For every ID in archiv, an abstract xml will be extracted with .efetch
    ### The use of xml in exchange of text, is to avoid an error with Entrez.read
    handle2 = Entrez.efetch(db = 'pubmed', id = ids, rettype = 'abstract', retmode = 'xml')
    record2 = Entrez.read(handle2)
    handle2.close()
    ### To access the actual abstract, the former xml will be used to acces the abstract field
    articulo = record2['PubmedArticle'][0]['MedlineCitation']['Article']
    ### If the ID file in question has no abstract, or the field is not found, it will be printed
    ### in the prompt so the user knows which article has no extractable abstract
    if 'Abstract' in articulo:
        abstract = articulo['Abstract']['AbstractText']
        ABSTRACTS.append(abstract)
        ### IDs of articles with abstracts will be saved for the next for cycle
        ABS2.append(ids)
    ### If an abstract can't be found, the user will get notified
    else:
        print("Articulo con ID [", ids, "] No posee 'abstract' extraible")

### Since IDs for citations will be appended, the file that will contain them must be
### created first
Lista_Citas = open("Uso_Entrez3.txt", "w")
Lista_Citas.write("")
Lista_Citas.close()

### This loop will help get the articles that cite the former articles
for arts in ABS2:
    ### .elink will enable the program to look for the citations of the article in question
    handle3 = Entrez.read(Entrez.elink(dbfrom="pubmed", db="pmc", id=arts))
    ### khe is a variable that helps to ensure the existance of citations
    khe = handle3[0]['LinkSetDb']
    if khe:
        ### If there are articles that cite the article in question, the list of IDs belonging to them will be
        ### saved in CITE
        CITE = [link["Id"] for link in handle3[0]["LinkSetDb"][0]["Link"]]
        ### The citing IDs will be appended also to "Uso_Entrez3.txt"
        Lista_Citas = open("Uso_Entrez3.txt", "a")
        Lista_Citas.write("Articulo "+arts+" es citado por "+str(CITE))
        Lista_Citas.close()
        ### The user will get notified about how many articles cite the article in question
        print("Hay", len(CITE), "articulos que citan a ", arts)
    else:
        ### If citations are not found, the user will be notified
        print("articulo", arts, "No es citado por el momento")
        ### CITE will return to be empty
        CITE = []

### To create the file that will contains the found abstracts
Lista_Abstracts = open("Uso_Entrez2.txt", "w")
Lista_Abstracts.write(str(ABSTRACTS))
Lista_Abstracts.close()
