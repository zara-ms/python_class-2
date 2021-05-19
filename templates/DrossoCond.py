'''

NAME
	DrossoCond.py

VERSION
	[1.0]

AUTHOR
	[Rodelmar Ocampo Luna] <joserodelmar@gmail.com>


DESCRIPTION
	[Programa que nos da el contenido de AT de las secuencias de cada linea en
	un archivo .csv y contesta 4 cuestiones diferentes acerca de otros elementos
	incluidos en cada linea del .csv usando listas y condicionales]

CATEGORY
	[analisis de secuencias]

USAGE
	[DrossoCond.py][-options/arguments]

ARGUMENTS
	[reader]  [var usada para leer el archivo .csv]
	[gene]  [var usada para leer cada linea del .csv]
	[pregunta_(1-4)]  [listas usadas para responder preguntas con condicionales]
	[line]  [var usada para el loop para trabajar en cada linea de gene]
	[fly_not]  [posicion de la primera coma en la linea]
	[fly]  [parte de la linea del .csv que contiene el nombre de la mosca]
	[sequence_not]  [posicion de la segunda coma]
	[sequence]  [parte de la linea del .csv que contiene la secuencia]
	[name_not]  [posicion de la tercera coma]
	[name]  [parte de la linea del .csv que contiene el nombre del gene]
	[express]   [parte de la linea que contiene la expresion del genee]
	[AT_content]    [Contenido de AT de sequence]

INPUT
	[archivo.csv dividido en 4 campos, nombre de la mosca, secuencia, nombre del gene, expresion]

OUTPUT
    [nombre y contenido de AT de cada gene, asi como la respuesta a 4 preguntas al final]

EXAMPLES
    [Example 1: 6-data.csv como input
    Program, Se lee cada linea del archivo .csv, y en el loop lo que se hace es
    separar cada linea en los campos que se necesitan para contestar las 4 preguntas
    y el contenido de AT de cada gene. Para contestar las preguntas, se van anadiendo
    elementos a las listas correspondientes para cada pregunta, si es que la linea en
    cuestion cumple con las condiciones al final de cada ciclo del loop]

GITHUB [https://github.com/Rodel-OL/python_class/blob/master/templates/DrossoCond.py]
'''
# Primero se abre y se lee con "with open as", usando a reader para leer
# las lineas y asignarle estas a gene
with open('6-data.csv', 'r') as reader:
    gene = reader.readlines()
# Despues de leer, siempre hay que cerrar
    reader.close()
# Se crean 4 listas que contestaran 4 preguntas acerca del contenido de cada linea
# las cuatro estan vacias, se les iran sumando elementos cada que una linea cumpla
# una condicion
pregunta_1 = []
pregunta_2 = []
pregunta_3 = []
pregunta_4 = []
# Para cada linea en gene, la variable line nos ayuda a pasar por cada linea
for line in gene:
# Como es un .csv, para obtener el nombre busca la primera coma en la linea,
# y la denomino como campo_not, para saber que esa es la posicion, no el
# segmento que se busca
    fly_not = line.find(",")
# El nombre de la mosca, fly, sera aquella parte que va desde el inicio hasta la primera coma
    fly = line[:fly_not]
# Misma logica, la secuencia esta entre la primera y la segunda coma, asi que en find
# busco desde la posicion en la que esta fly, +1 para que no cuente su coma
    sequence_not = line.find(",", fly_not+1)
# Ahora defino a sequence como el intervalo entre fly, y la coma despues de fly
    sequence = line[fly_not+1:sequence_not]
# Es el mismo procedimiento para los demas campos, busco desde la posicion anterior
# y delimito la secuencia hasta donde se encuentra otra coma
    name_not = line.find(",", sequence_not+1)
    name = line[sequence_not+1:name_not]
    express = line[name_not+1:]
# Para obtener el contenido de AT, se cuentan y suman las a y t en sequence, y se divide entre lo que mide
# sequence
    AT_content = (((sequence.count("a"))+(sequence.count("t")))/len(sequence))
# Imprimo tanto el nombre, como el contenido de AT, y si es alto, medio o bajo para cada secuencia
    print(name)
    print(AT_content)
    if (AT_content > 0.65):
        print("Contenido de AT alto")
    elif (AT_content > 0.45 and AT_content < 0.65):
        print("Contenido de AT medio")
    elif (AT_content < 0.45):
        print("Contenido de AT bajo")
# Si el gene pertenece a ya sea Drosophila melanogaster o simulans, el nombre pasa a formar parte de
# la lista de pregunta_1
    if (fly == "Drosophila melanogaster" or fly == "Drosophila simulans"):
        pregunta_1.append(name)
# Si la secuencia es de entre 90 y 110 bases de largo, el nombre del gene se suma a
# pregunta_2
    if (len(sequence)>90 and len(sequence)<110):
        pregunta_2.append(name)
# Si el contenido de AT de la secuencia es menor a 0.5, y su expresion es mayor a 200
# el elemento se suma a pregunta_3. como express es un string, necesitamos convertirlo a
# int para compararlo con 200, por lo que usamos int()
    if (AT_content<0.5 and int(express)>200):
        pregunta_3.append(name)
# Si el nombre de la mosca no es Drosophila melanogaster, y el nombre del gene empieza o con
# h o con k, el elemento se suma a pregunta_4
    if (fly != "Drosophila melanogaster" and name.startswith("k") or name.startswith("h")):
        pregunta_4.append(name)
# Despues de imprimir los conteidos de AT y nombres de cada gene, se contestan las preguntas
# con las listas a las cuales se les fueron anadiendo elementos si estos cumplian las condiciones antes
# mencionadas y repetidas en los print
print("Genes de Drosophila melanogaster y simulans:", pregunta_1)
print("Genes de entre 90 y 110 bases de longitud:", pregunta_2)
print("Genes con contenido de AT menor a 0.5 y expresion mayor a 200:", pregunta_3)
print("Genes que empiezan con h o k que no son de Drosophila melanogaster:", pregunta_4)
