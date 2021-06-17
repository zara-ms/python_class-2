'''

NAME
	DNAmino.py

VERSION
	[1.0]

AUTHOR
	[Jose Rodelmar Ocampo Luna] <joserodelmar@gmail.com>
	[Other authors]: [Modifications]


DESCRIPTION
	[Programa que traduce una secuencia de RNA en los aminoacidos
	que codifica, en formato de una letra]

CATEGORY
	[Analisis de Secuencias]

USAGE
	[DNAmino.py][-options/arguments]

ARGUMENTS
	[seq]  [Se usa en la funcion DNAonly para tratar la cadena
	        de RNA para ser traducida]

FUNCTIONS
    [DNAonly]  [seq]

INPUT
	[Secuencia de RNA]

NOT WORKING INPUT
    [Si el string de la secuencia de RNA no tiene un largo que sea
    multiplo de 3, el programa no funciona]

OUTPUT
    [Tripletes o codones de DNA, junto con aminoacidos codificados]

EXAMPLES
    [input="AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    programa va a tratar con DNAonly la cadena para pasarla a DNA
    y dividirla en tripletes
    output=
    Estos serian tus tripletes como codones de DNA: ['ATG', 'GCC', 'ATG', 'GCG', 'CCC', 'AGA', 'ACT', 'GAG',
     'ATC', 'AAT', 'AGT', 'ACC', 'CGT', 'ATT', 'AAC', 'GGG', 'TGA']
    Este seria el aminoacido que codifican: ['M', 'A', 'M', 'A', 'P', 'R', 'T', 'E', 'I', 'N', 'S', 'T', 'R', 'I',
    'N', 'G', '_']]

GITHUB
    [https://github.com/Rodel-OL/python_class/blob/master/templates/DNAmino.py]

'''
# Se le pide al usuario una cadena de RNA cuyo largo sea divisible entre 3
# y esa cadena se guarda en amino
print("Dame una cadena de RNA cuyo largo sea multiplo de 3")
amino = input()
# aminofinal almacenara los aminoacidos codificados en la secuencia
aminofinal = []
# DNA almacenara la cadena amino tratada para ser traducida
DNA = []
# en gencode se tienen los tripletes de DNA, y el aminoacido que
# codifican, es un diccionario
gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T',
    'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N',
    'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R',
    'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
    'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
    'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V',
    'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
    'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S',
    'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
    'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
# Funcion DNAonly que trata la cadena de RNA para su traduccion
def DNAonly(seq):
    # Las U se reemplazan por T, para pasar de RNA a DNA, que es
    # lo que usa gencode
    seq2 = seq.replace("U", "T")
    # lon nos da el largo de la secuencia
    lon = len(seq2)
    # En el for, lo que se quiere es que en intervalos de 3, la
    # secuencia de DNA se vaya guardando en la lista DNA
    for i in range(0, lon, 3):
        # En codon se van guardando los tripletes o codones
        codon = seq2[i:i + 3]
        DNA.append(codon)
    return
# La secuencia amino es tratada con la funcion DNAonly
DNAonly(amino)

# Para cada elemento o triplete en lista DNA, se va a buscar el
# "value" correspondiente, es decir, el aminoacido que codifica
# y este se ira anadiendo a la lista aminofinal
for triplets in DNA:
    # cod va guardando el aminoacido codificado
    cod = gencode.get(triplets)
    aminofinal.append(cod)

# Se le imprimen a pantalla al usuario, sus codones de DNA
# y el aminoacido que codifican
print("Estos serian tus tripletes como codones de DNA:", DNA)
print("Este seria el aminoacido que codifican:", aminofinal)
