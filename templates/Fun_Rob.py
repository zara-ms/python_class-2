'''

NAME
	Fun_Rob.py

VERSION
	[1.0]

AUTHOR
	[Rodelmar Ocampo Luna] <joserodelmar@gmail.com>
	[Other authors]: [Modifications]


DESCRIPTION
	[This program contains a function that allows the user to know the percentage of hidrophilic aminoacids
	contained in his proteic sequence using this sequence and a given aminoacid as parameters]

CATEGORY
	[sequence analysis]

USAGE
	[Fun_Rob.py][-options/arguments]

ARGUMENTS
	[amino_per]  [name of the function]
	[protein_seq]  [input, one of the parameters of the function, were the proteic sequence goes]
	[amino]  [input, another function parameter, here the user logs the aminoacid in question]
	[amino_seq]  [var where proteic sequence is turned into a homogenic amino sequence]
	[amino_count]   [the number of times the given amino appears in the sequence]
	[amino_content] [The percentage of the given aminoacid within the sequence]
	[aa_list]   [List of Hidrophylic aminoacids]
	[hi_a]  [var used in the for to use the function with every element contained in aa_list]

INPUT
	[protein_seq]
	[amino]

OUTPUT
    [the percentage of hidrophylic aminoacids contained in the sequence]

EXAMPLES
    [Example 1:  "MSRSLLLRFLLFLLLLPPLP", hi_a , and a given aa_list with hidrophylic aminoacids in a for as an input
    Program, for every amino in aa_list, as hi_a on the for, the sequence is homogenized,
     and then and the given amino is searched for. After counting the times it appears, it calculates
      the percentage of it due to the sequence length
      Output, 0.0
            0.0
            50.0
            5.0
            10.0
            0.0
            0.0
            0.0
            50.0]

GITHUB [https://github.com/Rodel-OL/python_class/blob/master/templates/Fun_Rob.py]
'''
def amino_per(protein_seq, amino):
    amino_seq = protein_seq.upper()
    amino = amino.upper()
    amino_count = amino_seq.count(amino)
    amino_content = (amino_count / len(amino_seq)*100)
    print(amino_content)
    return (amino_content)
aa_list=['A','I','L','M','F','W','Y','V']
for hi_a in aa_list:
    amino_per("MSRSLLLRFLLFLLLLPPLP", hi_a)
