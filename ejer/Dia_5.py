### EGQuery
from Bio import Entrez
Entrez.email = "joserodelmar@gmail.com"

### termino = "(Aedes[Title] OR Aedes[All Fields])AND((RNA-Seq[Title] OR transcriptomic[Title]) OR (transcriptome[Title] OR sequencing[Title]))"
### handle = Entrez.egquery(term=termino)
### record = Entrez.read(handle)
### handle.close()
### for row in record["eGQueryResult"]:
    ### print(row["DbName"], row["Count"])
### En pubmedhealth marca un error

### ESpell

### handle = Entrez.espell(term="biopythooon")
### record = Entrez.read(handle)
### record["Query"]
### (hasta aqui senala que esta mal escrito)
### record["CorrectedQuery"]
### (Y acorregido)

### Esummary (resumen de la lista de IDs)
### handle = Entrez.esummary(db="taxonomy", id="9913,30521")
### record = Entrez.read(handle)
### handle.close()
### print(record[0].keys())
### print(record[0]["Id"])
### print(len(record))
### |
### v
### Checar tamanos con Esummary
### import pickle
### print(len(pickle.dumps(record)))

### Efetch
### from Bio import Seq.IO
### Entrez.efetch(base de datos, id, tipo, modo)
### handle = Entrez.efetch(db="nucleotide", id="HE805982", rettype="gb", retmode="text")
### record = SeqIO.read(handle, "genbank")
### handle.close()
### Tmbn podemos acceder a record.id | .description | .annotations | .seq |
### print(record)
### Entrez.read(handle) no funciona en lugar de handle.read, porque necesita un binario

### Guardar archivo
### Primero asignas un string a la variable para el for
### filename = "HE805982.gb"
### Con lo que se busca con efetch, como un archivo, Se abre y se escriibe en el filename como si fuera handle
### with Entrez.efetch(db="nucleotide",id="HE805982",rettype="gb", retmode="text") as file:
    ### with open(filename, "w") as handle:
        ### handle.write(file.read())
### handle.close()
### record = SeqIO.parse("HE805982.gb", "genbank")
### Aqui se usa parse porq se tiene mas de 1
### print(record)

### Hay que usar read.handle en lugar de Entrez.read
### out_handle = open("prueba.fasta", "w")
### fetch_handle = Entrez.efetch(db="nucleotide", id="1919569438, 1919569357, 1251949171",
                            ### rettype="fasta", retmode="text")
### data = fetch_handle.read()  #usar handle.read()
### fetch_handle.close() #cerrar handle
### out_handle.write(data) #escribir archivo
### out_handle.close() #cerrar archivo

#____Ejercicio_2____
### Buscar linajes, que tan emparentados estan dos organismos
### [Notoryctes typhlops] y [Chrysochloris asiatica]
handle = Entrez.esearch(db="Taxonomy", term="Notoryctes typhlops")
record = Entrez.read(handle)
print(record["IdList"])
handle.close()
### Con esto, obtenemos el ID del organismo que buscamos en la base de datos de Taxonomy

id_taxo = record["IdList"]
handle = Entrez.efetch(db="Taxonomy", id=id_taxo, retmode="xml")
Notoryctes = Entrez.read(handle)
print(Notoryctes[0].keys())
### Vemos que esta Lineage, que es el que nos interesa, y ponemos
print(Notoryctes[0]["Lineage"])
handle.close()
### Y se repite lo mismo con el otro organismo
### Ahora, como se pueden comparar
handle2 = Entrez.esearch(db="Taxonomy", term="Chrysochloris asiatica")
record2 = Entrez.read(handle2)
id_taxo2 = record2["IdList"]
handle2 = Entrez.efetch(db="Taxonomy", id=id_taxo2, retmode="xml")
Chrysochloris = Entrez.read(handle2)
print(Chrysochloris[0]["Lineage"])
handle2.close()
print(Notoryctes[0]["Lineage"])
Not = (Notoryctes[0]["Lineage"])
Not2 = Not.split(";")
Chrys = (Chrysochloris[0]["Lineage"])
Chrys2 = Chrys.split(";")
def comparar(org1, org2):
    i = 0
    for lin1, lin2 in zip(org1, org2):
        if lin1 == lin2:
            i = i+1
        else:
            break
    return i
print(comparar(Not2, Chrys2))

###Elink
### ids = "15718680"
### ids puede tener mas de un ID
### record = Entrez.read(Entrez.elink(dbfrom="protein", id=ids,db='gene'))
### recuerda que hay que importar pprint
### pprint(record[0])

### Para que aparezcan mas de uno en el orden que se solicito
### Primero con una funcion se cambia de
### id=15718680%2C157427902 a id=15718680&id=157427902
### from urllib.request import urlopen
### from urllib.parse import urlencode
### def elink_multiple(dbfrom, ids, db, mirror="https://eutils.ncbi.nlm.nih.gov/entrez/eutils"):
    # diccionario con lo que tendrá el URL
    ### parameters = {"dbfrom": dbfrom, "db":db, "id": ids, "tool":"biopython", "email":Entrez.email}
    # Creamos la URL
    ### command = urlencode(parameters, doseq=True)
    ### url = "%s/elink.fcgi?%s" % (mirror, command)
    ### handle = urlopen(url)
    ### return(handle)

### Elink multiple
### pmids = ["15718680","157427902"] # ids a buscar
### handle = elink_multiple(dbfrom="protein", ids=pmids, db="gene")
### handle.url
### record = Entrez.read(handle)
### handle.close()
### pprint(record[1])

###Obtener citas
### pmid = "32703847" #pubmed id
### results = Entrez.read(Entrez.elink(dbfrom="pubmed", db="pmc", id=pmid))
### pprint(results[0])

### Encontrar eponimos (https://pubmed.ncbi.nlm.nih.gov/34434786/)

###Para busquedas mas especificas
### results = Entrez.read(Entrez.elink(dbfrom="pubmed", db="pmc", LinkName="pubmed_pmc_refs", from_uid=pmid))
### Aqui esta en el orden pubmed_pmc_refs, pero lo podemos cambiar a pmc_refs_pubmed en LinkName y id=",".join(pmc_ids)
# para IDs para pubmed
### pmc_ids = [link["Id"] for link in results[0]["LinkSetDb"][0]["Link"]]
### print(pmc_ids)

### EPost
