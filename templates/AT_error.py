'''

NAME
	AT_error.py

VERSION
	[1.0]

AUTHOR
	[Rodelmar Ocampo Luna] <joserodelmar@gmail.com>


DESCRIPTION
	[Programa que con la funcion get_AT_content da el porcentaje de AT
	de las secuencias introducidas. Ademas, este programa maneja errore
	como el no encontrar el archivo input, y tener valores errados como
	"N"]

CATEGORY
	[analisis de secuencias]

USAGE
	[AT_error.py][-options/arguments]

ARGUMENTS
	[seq]  [Se usa en la funcion get_AT_content, secuencia a analizar]

INPUT
	[archivo.txt con las seceuncias, cada linea es evaluada]

OUTPUT
    [AT_content_sequences.txt con los porcentajes de AT de cada secuencia, por linea]

EXAMPLES
    [Example 1: 4_dna_sequences.txt como input
    Program, Se lee cada linea del archivo.txt, y despues se pasan a la funcion
    get_AT_content, en donde son tratadas para ser mayusculas, y obtener el porcentaje
    de As y Ts. Los resultados se guardan en otro archivo.txt llamado AT_content_sequences.txt
    y si existen errores en la ubicacion o contenido del archivo input, se imprime
    un mensaje correspondiente]

GITHUB []
'''
#Para poder introducir el input desde la linea de comando
import sys
arguments = sys.argv
file_path = arguments[1]
print("Que archivo quieres usar?")
#Usando with open as, se usa la variable reader para leer las lineas, que se
# almacenaran en la variable all_lines
with open (input(), 'r') as reader:
    all_lines = reader.readlines()
    reader.close()

def get_at_content (seq):
#Primero se pasan a mayusculas las letras en la linea
    seq_mat = seq.upper()
#Se busca que no existan Ns en las lineas a analizar, si las hay, se marcara el error y cuantas
# Ns hay en la linea
    if seq_mat.count("N") > 0:
        raise ValueError(f'Tu seceuncia tiene {seq_mat.count("N")} N\'s')
#Se cuenta por separado el contenido de As y Ts, para despues esa suma dividirla entre el total de la secuencia
    A_cont = seq_mat.count("A")
    T_cont = seq_mat.count("T")
    AT_cont = ((A_cont+T_cont))/(len(seq))
#La funcion regresa el contenido de AT en AT_cont
    return(AT_cont)
try:
#Con open with as, se busca escribir en el nuevo archivo output, cada linea
# del nuevo archivo correspondera a las lineas en all_lines
    with open('AT_content_sequences.txt', 'w') as writer:
        for line in all_lines:
#Se escribe en cada linea el contenido de AT de cada secuencia como un string
            writer.write(str(get_at_content(line)) + "\n")

    writer.close()
#Si el archivo input no se encuentra, el programa lo va a marcar
except IOError:
    print("Hubo un error, no se pudo encontrar tu archivo")
#Si hay un valor, letra, en la secuencia como la N, se va a marcar el error
except ValueError:
    print("Hubo un error en los valores introducidos")
