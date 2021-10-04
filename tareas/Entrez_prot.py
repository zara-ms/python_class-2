'''

NAME
	Entrez_prot.py

VERSION
	[1.0]

AUTHOR
	[Ocampo Luna Jose Rodelmar] <joserodelmar@gmail.com>
	[Other authors]: [Modifications]


DESCRIPTION
	[This program uses Entrez form BioPython to acces and read the
	description of the fields ECNO (in FieldList) and
	protein_protein_small_genome (in LinkList) from the databese
	"protein"]

CATEGORY
	[category of the program: DataBase analysis]

USAGE
	[Entrez_prot.py][-options/arguments]

ARGUMENTS
	[field]  [used in the for cycle corresponding to the search in FieldList]
	[linker]  [used in the for cycle corresponding to the search in LinkList]

INPUT
	[No input required, searched names already embeded]

NOT WORKING INPUT
    [Input option is non existent]

OUTPUT
    [print of the description of both fields ECNO and protein_protein_small_genome]

EXAMPLES
    [Program is run
    >ECNO : EC number for enzyme or CAS registry number
    protein_protein_small_genome : All proteins from this genome]

GITHUB
    [https://github.com/Rodel-OL/python_class/blob/master/tareas/Entrez_prot.py]

'''
from Bio import Entrez
Entrez.email = "joserodelmar@gmail.com"
### handle is used to access the data base
handle = Entrez.einfo(db="protein")
### record is used to "read" the elemnts accessed in handle
record = Entrez.read(handle)
### After use, it is important to close the access
handle.close()

### DbInfo and FieldList are accessed through the reader in record
for field in record["DbInfo"]["FieldList"]:
    ### When the name in FieldList matches "ECNO". the desciption of such can be printed
    if field["Name"] == "ECNO":
        print(field["Name"], ":", field["Description"])

### Second for cycle works the same, only FieldList is replaced with LinkList and
### the name of field searched becomes "protein_protein_small_genome"
for linker in record["DbInfo"]["LinkList"]:
    if linker["Name"] == "protein_protein_small_genome":
        print(linker["Name"], ":",  linker["Description"])
