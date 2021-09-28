from Bio import PDB
#Para crear el objeto, se crea el objeto parser, que
#nos parsea, lo cual es necesario para parsear los datos
parser = PDB.PDBParser(QUIET=True)
path2 = "1kcw.pdb"
structure = parser.get_structure("prot_1kcw", path2)
#print(structure.get_id)
print(structure.header['structure_method'])
print(structure.header['resolution'])

###cys_A = []
### for model in structure:
    ### for chain in model:
        ### residue = chain[22]
        ### print(residue.get_resname())
            ### for atom in residue:
                ### print(atom)
                ### atom_ca = residue['CB']
                ### print(atom_ca.coord)
                ### print(atom_ca.element)
                ### print(atom_ca.id)

### residue = chain[22]
### print(residue.get_resname())

### for atom in residue:
    ### print(atom)

### atom_ca = residue['CB']

### print(atom_ca)

### print(atom_ca.coord)

### print(atom_ca.element)
### print(atom_ca.id)

### Otros metodos para obtener child
### chainss = model.get_chains()
### print(chainss)
### Con esto podemos iterar sin los for anteriores
### residuess = chain.get_residues()
### print(*residuess)
###

### Ejercicio_3
cisteinas = []
for modelo in structure:
    for chain in modelo:
        if chain.id == 'A':
            for residuo in chain:
                if residuo.get_resname() == 'CYS':
                    cisteinas.append(residuo)
for atom in cisteinas[0]:
    print(atom.element, atom.id)
### Si resto dos atomos, me da la distancia entre ellos
### atom_1 = residuo['N']
### atom_2 = residuo['CA']
### print(atom_1 - atom_2)

### Ejercico 4
pares = []
for cys1 in cisteinas:
    for cys2 in cisteinas[1:]:
        distancia = (cys1['SG']-cys2['SG'])
        if((distancia)<8):
            print(cys1['SG'].coord, cys2['SG'].coord)
            print(cys1.id, cys2.id)
