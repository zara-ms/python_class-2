from Bio.Seq import Seq
from Bio.Seq import MutableSeq
seqobj = Seq("ATCTAGCTAGTTAGACG")
print(seqobj.complement())
print(seqobj.reverse_complement())
print(seqobj.translate(to_stop=True))

import re

for codon in re.findall(r"(.{3})", str(seqobj)):
    print(codon)

from Bio.SeqUtils import nt_search

patron = Seq("ACG")
sequence = Seq("ACTGAGCTAGCTGACCACGACGTGAGCTAACG")
resultado = nt_search(str(sequence), patron)
print(resultado)

#Segunda parte despues del ejercicio
from Bio import SeqIO
filename = ""
for seq_record in SeqIO.parse(filename, "fasta"):
    print("ID {}".format(seq_record.id))
    print("len {}".format(len(seq_record)))
    print("Traduccion {}".format(seq_record.translate(to_stop=True)))


resultado2 = nt_search(str(sequence),patron.reverse_complement())
print(resultado2)

print(GC(sequence))
print(molecular_weight(sequence))

#Leer archivo en diccionario
id_dict = SeqIO.to_dict(SeqIO.parse(filename,"fasta"))

