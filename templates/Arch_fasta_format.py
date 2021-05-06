'''

NAME
	Arch_fasta_format.py

VERSION
	[1.0]

AUTHOR
	[Rodelmar Ocampo Luna] <joserodelmar@gmail.com>
	[Other authors]: [Modifications]


DESCRIPTION
	[This program formats a txt file with just a header and sequences, and gives it a fasta format]

CATEGORY
	[sequence format]

USAGE
	[Arch_fasta_format.py][-options/arguments]

ARGUMENTS
	[reader]  [var used to open the .txt file]
	[writer]  [var used to write in the .txt file]
	[dna-seq]  [var used to read all the lines of .txt once opened]
	[line]  [var used for the loop to write on every "line" on the file]

INPUT
	[DNA sequences with headers contained in 4_dna_sequences.txt file]

OUTPUT
    [same input file, but with sequences in fasta format]

EXAMPLES
    [Example 1: 4_dna_sequences.txt as an input
    Program, for every line in input file, adds ">" to headers
    and homogenizes the letters of the sequences, so it becomes a file in
    a fasta format, with the same sequences]

GITHUB [https://github.com/Rodel-OL/python_class/blob/master/templates/Arch_fasta_format.py]
'''

## First, open and read using "with" and "as"
with open('4_dna_sequences.txt', 'r') as reader:
## dna_seq is used to access all the lines in the files
    dna_seq = reader.readlines()
    reader.close()
## Second, write on the file using with open as
with open('4_dna_sequences.txt', 'w') as writer:
## writer.write to actually write on the file. Loop for every line in .txt
    for line in dna_seq:
## first, write until the 5 position of the line, which will become the header of the sequence
## Second, next part will come form position 8 till the end of the line, and it most be homozygous, all continious and in upper class
        writer.write("> " + line[:5] + '\n' + line[8:].replace('"', "").replace("-", "").upper() + '\n')
    writer.close()
