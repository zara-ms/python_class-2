'''

NAME
	Res_PDB.py

VERSION
	[1.0]

AUTHOR
	[Rodelmar Ocampo] <joserodelmar@gmail.com>
	[Other authors]: [Modifications]


DESCRIPTION
	[The function within this program allows the user to obtain
	the specific residues of a determined chain and path
	from a PDB file. This residues are saved in a list, which
	is returned by the function within]

CATEGORY
	[category of the program: PDB file analysis]

USAGE
	[residues_pdb(pdb_path, specified_chain, search_residue)]

ARGUMENTS
	[pdb_path]  [path of the .pdb file]
	[specified_chain]  [chain of the .pdb file from which
	                    the user wishes to take residues from]
	[search_residue]  [specified residue to search]

FUNCTIONS
    [residues_PDB]  [pdb_path, specified_chain, search_residue]

INPUT
	[pdb_path : path towards an existing .pdb file]
	[specified_chain : existing chain in the .pbd file]
	[search_residue : residue expressed in the 3 letter code
	                for aminoacids]

NOT WORKING INPUT
    [pdb_path : a non existing path, or a non .pdb file]
    [specified_chain : a non existing character in the .pdb file]
    [search_residue : any set of characters not contained
                        in the three letter code of aminoacids]

OUTPUT
    [List with enumerated residues acquired from specified
    path and chain along with it's location]

EXAMPLES
    [print(residues_pdb("1kcw.pdb", "A", "CYS"))
    > ['CYS_1[<Residue CYS het=  resseq=155 icode= >]',
    'CYS_2[<Residue CYS het=  resseq=181 icode= >]',
    'CYS_3[<Residue CYS het=  resseq=221 icode= >]',
    'CYS_4[<Residue CYS het=  resseq=257 icode= >]',
    'CYS_5[<Residue CYS het=  resseq=319 icode= >]',
    'CYS_6[<Residue CYS het=  resseq=338 icode= >]',
    'CYS_7[<Residue CYS het=  resseq=515 icode= >]',
    'CYS_8[<Residue CYS het=  resseq=541 icode= >]',
    'CYS_9[<Residue CYS het=  resseq=618 icode= >]',
    'CYS_10[<Residue CYS het=  resseq=680 icode= >]',
    'CYS_11[<Residue CYS het=  resseq=699 icode= >]',
    'CYS_12[<Residue CYS het=  resseq=855 icode= >]',
    'CYS_13[<Residue CYS het=  resseq=881 icode= >]',
    'CYS_14[<Residue CYS het=  resseq=1021 icode= >]']
    ]

GITHUB
    [https://github.com/Rodel-OL/python_class/blob/master/tareas/Res_PDB.py]

'''
from Bio import PDB
### We need a parser to access the information in the .pbd file
parser = PDB.PDBParser(QUIET=True)

def residues_pdb (pdb_path, specified_chain, search_residue):
    ### structure is used for parsing the input path
    structure = parser.get_structure("prot_pdb", pdb_path)
    ### i is a variable that works as a counter for the elements in the returned list
    i = 0
    ### res_list will save the residues that match the input parameters
    res_list = []
    ### the archive as structure is subdivided as "model"
    for model in structure:
        ### Within the subdivision of model, the category of chains can be accessed
        for chains in model:
            ### If the ID of the chain matches the input chain, it can enter the next loop
            ### for residue searching
            if chains.id == specified_chain:
                for residues in chains:
                    ### get_resname from the chain's residue must match the searching residue
                    if residues.get_resname() == search_residue:
                        ### for each matching residue found, the counter will advance 1
                        i = i + 1
                        ### the appended element will have the searched residue name enumerated along with the
                        ### information associated with it's location in the file
                        res_list.append(search_residue + '_' + str(i)+"["+str(residues)+"]")

    ### The returned value is the residues list with their location information
    return res_list

print(residues_pdb("1kcw.pdb", "A", "CYS"))

