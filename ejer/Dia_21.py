from Bio import PDB
#Para crear el objeto, se crea el objeto parser, que
#nos parsea, lo cual es necesario para parsear los datos
parser = PDB.PDBParser(QUIET=True)

#Sintaxis
#obj_struc = parser.get_structure("nombre", "archivo.pdb")

path = "1fat.pdb"
struc = parser.get_structure("prot_1fat", path)
print(struc.child_dict)
print(struc.child_list)

#Metadatos

#struc.atributo_metadato[]
#print(struc.header.keys())
#print(struc.header['structure_method'])
#print(struc.header['resolution'])

# Crear un objeto structure con el archivo 1kcw.pdb e
# imprimir el método con el que se creó el modelo y
# su resolución
path2 = "1kcw.pdb"
structure = parser.get_structure("prot_1kcw", path2)
#print(structure.get_id)
print(structure.header['structure_method'])
print(structure.header['resolution'])

#Ver cada uno de los valores dentro de los metadatos
#for key, valor in structure.header.items():
    #print(key, valor)

# Archivo de resonancia magnética nuclear
## struct = parser.get_structure('RMN', "./files/clase_3/1g03.pdb")
## for model in struct:
    ## print(model)
        #Cadenas
    ## for chain in model:
        ## print(chain)
        ## for residue in chain:
            ## print(residue)
            ## <Residue SER het=  resseq=1 icode= >
            ## <Residue ASN het=  resseq=2 icode= >
            ## Como lista seria (residue = chain[1])
            # ID
            ## residue.get_id()[1]
            ## residue.get_resname()
            # Ubicar en especific
            ## if residue.get_resname() == "PHE":
            ##    print(residue)
# Guardar en una lista todas las cisteínas de la
# cadena A del archivo 1kcw.pdb

cys_A = []
for model in structure:
    for chain in model:
        if chain.id == 'A':
            for residue in chain:
                if residue.get_resname == 'CYS':
                    cys_A.append(residue)

print(len(cys_A))