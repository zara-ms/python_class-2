from Bio import Entrez
### from pprint import pprint
### Siempre debes de tenr un correo para entrar
Entrez.email = "joserodelmar@gmail.com"
handle = Entrez.einfo(db="genome")
result = handle.read()
print(result)
### Obtenemos diccionario (llave "DBlist")
record = Entrez.read(handle)
print(record["DbList"][0:3])
print(record["DbInfo"]["Description"])
print(record["DbInfo"]["FieldList"])
### Para sacar el url debido
print(handle.url)
handle.close()
### Ejercicio_1
i = -1
for field in record["DbInfo"]["FieldList"]:
    i = i+1
    if field["Name"] == "ORGN":
        print(field["NAME"], field["Description"])
        print(record["DbInfo"]["FieldList"][i]["Description"])
### Esearch
### Entrez.esearch( base de datos a buscar , termino )
    ### handle = Entrez.esearch(db = "pubmed", term = "biopython")
    ### record = Entrez.read(handle)
    ### print(record["Count"])
    ### print(handle.url)
    ### handle.close()

### retmax
###  len(record["IdList"])  #chequemos tamaño
### count = int(record["Count"]) #cambiemos retmax por long de Counts
### handle = Entrez.esearch(db="pubmed", term="biopython", retmax=count)
### record = Entrez.read(handle)
### handle.close()
### len(record["IdList"])

### Buscando Autores
handle = Entrez.esearch(db="pubmed", term='Valeria Mateo_Estrada', field='AUTH')
###                                                                     |
###                                                                     V
###                                                                  ['AUTH']
record = Entrez.read(handle)
handle.close()

### Busqueda compleja
### termino = "(Aedes[Title] OR Aedes[All Fields])AND((RNA-Seq[Title] OR transcriptomic[Title]) OR (transcriptome[Title] OR sequencing[Title]))"
### handle = Entrez.esearch(db="pubmed", term=termino)
### result = Entrez.read(handle)
### print(result["Count"])
