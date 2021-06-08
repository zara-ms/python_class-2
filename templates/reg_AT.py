'''

NAME
	reg_AT.py

VERSION
	[1.0]

AUTHOR
	[Rodelmar Ocampo] <joserodelmar@gmail.com>
	[Other authors]: [Modifications]


DESCRIPTION
	[Programa que verifica la existencia de una secuencia de ATGC
	e imprime las regiones con AT. En el caso de no existir ATGC
	se imprimen las regiones con AT que no tienen GC despues para
	indicar donde esta el error]

CATEGORY
	[Analisis de secuencias]

USAGE
	[reg_AT.py][-options/arguments]

ARGUMENTS
	[seq]  [Se usa en la funcion conATGC, almacena la secuencia a analizar]

INPUT
	[Se usa la variable dna en la funcion conATGC]

NOT WORKING INPUT
    [Se puede introducir en dna cadenas o archivos con ruta correcta]

OUTPUT
    [Si hay ATGC, se communica al usuario, y se imprimen las regiones con AT
    Si no hay ATGC, se comunica al usuario y se le imprimen las secuencias
    con el error]

EXAMPLES
    [input> dna = "CTGCATTATATCGTACGAAATTATACGCGCG"
    La funcion conATGC determinara si la secuencia introducida tiene
    o no ATGC. Esta no la tiene
    output> Hubo un error en los valores introducidos
    En vez de ATGC, tienes: <re.Match object; span=(4, 8), match='ATTA'>
    En vez de ATGC, tienes: <re.Match object; span=(9, 13), match='ATCG'>
    En vez de ATGC, tienes: <re.Match object; span=(19, 23), match='ATTA'>
]

GITHUB
    [https://github.com/Rodel-OL/python_class/blob/master/templates/reg_AT.py]

'''

## importar re para poder trabajar con expresiones regulares
import re
## Funcion que define si hay ATGC en una secuencia dada
def conATGC (seq):
    ## Si hay minusculas, se deben de pasar a mayusculas para que trabaje la funcion
    seq_mat = seq.upper()
    ## Se busca que haya ATGC con .search, y si hay se envia mensaje
    if (re.search('ATGC', seq_mat)):
        return ("Secuencia contiene ATGC")
    else:
        ## En caso de no tener ATGC, se comunica al usuario
        raise ValueError(f'Tu secuencia no tiene ATGC, vuelve a intentarlo')

dna = "CTGCATTATATCGTACGAAATTATACGCGCG"
## Prueba de errores, en try, si la funcion conATGC no regresa error
## Se imprimen las regiones con AT
try:
    print(conATGC(dna))
    regions = (re.finditer(r"AT",dna))
    for reg in regions:
        print(reg)
except ValueError:
    ## Si conATGC no encuentra ATGC, se indica
    print("Hubo un error en los valores introducidos")
    ## Se imprimen las secuencias que contienen AT mas otras dos bases
    ## cualesquiera que no son GC
    mistake = re.finditer(r"AT..", dna)
    for mis in mistake:
        print("En vez de ATGC, tienes:", mis)
