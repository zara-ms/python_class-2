
dna = "AAGGATGTCGCGCGTTATTAGCCTAA"
inicio = dna.find("ATG")
final = dna.find("TAA")
InmaSeq = dna[inicio:final+3]
MatSeq = InmaSeq.replace("T", "E").replace("G", "F").replace("A", "U").replace("C", "G")
MatuSeq = MatSeq.replace("E", "A").replace("F", "C")
print("El codon de inicio empieza en posicion: ", inicio)
print("Y la secuencia transcrita termina en :", final+3)
print("La secuencia transcrita de rna es :", MatuSeq)
'''
#NAME
#Sec_inicio_final_trans.py

#VERSION
#[  1 .2]

#AUTHOR
#[Rodelmar Ocampo] < joserodelmar@gmail.com >
#[Other authors]: [Modifications]

#DESCRIPTION
#[Program to obtain a transcribed RNA sequence from a DNA sequence. Start and stop codons positions also displayed]

#CATEGORY
#[sequence analysis]

#USAGE
#[Sec_inicio_final_trans.py][-options / arguments]

#ARGUMENTS
#[dna][Where the input DNA sequence goes]
#[inicio][seeks for a start codon]
#[final][seeks for a stop codon]
#[InmaSeq][Inmature sequence, only defined as the DNA between sstart and stop positions]
#[MatSeq][Mature sequence in progress, prime step before an actual mature sequence. Half of complementary bases]
#[MatuSeq][Actual mature sequence. The another half of bases with no Watson-Crick unions are fixed]

#INPUT
#[sequences of DNA]

#OUTPUT
#[Start codon position_Stop codons position_transcribed sequence]

#EXAMPLES
#[Example 1: describe the example, El codon de inicio empieza en posicion: 1 
#Y la secuencia transcrita termina en : 6
#La secuencia transcrita es : UACAACUAG]


'''


## 1. [ Introduce a valid DNA sequence]

## 2. [ Execute the program]

