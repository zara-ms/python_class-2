### Aplicaciones de numpy
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
count_matrix = np.array([ [3, 3, 0],
                          [0, 0, 1],
                          [1, 1, 0],
                          [0, 0, 1],
                          [1, 0, 4],
                          [1, 2, 0]])
### Matriz de coexpresion
count_matrix = np.where(count_matrix > 0, 1, 0)
print(count_matrix)
### Comparar gen con gen
print(count_matrix.T[0])
print((count_matrix.T[0]) & (count_matrix.T[0]))
print(sum((count_matrix.T[0]) & (count_matrix.T[0])))
### producto punto
print(np.dot(count_matrix.T[0], count_matrix.T[0]))
### gen 1 contra gen 3
print(np.dot(count_matrix.T[0], count_matrix.T[2]))
### Para visualizar
print(np.vstack((count_matrix.T[0], count_matrix.T[2])))
###Multiplicacion
print(np.matmul(count_matrix.T,count_matrix))
### Ploteo
#import matplotlib.pyplot as plt
#import networkx as nx
plt.imshow(expresion)
plt.colorbar()
plt.show()

G = nx.DiGraph(expresion)
nx.draw(G, node_size = 900,  with_labels=True)
plt.show()

### Secuencias
from Bio.Seq import Seq
import numpy as np
# Hay que resolver lo del problema mutable y no mutable
p = [0.5,0.5,0.5,0.5]
def secuencia_aleatoria(tamano = 100, param = p,seed = None):
    np.random.seed(seed) # posibilidad de reproducibilidad
    DNA = list("ATGC")
    #secuencia random con distribucion p
    secuencia = Seq(''.join(np.random.choice(DNA, tamano, p)))
    return(secuencia)
# prueba
p = [0.1,0.2,0.4,0.3]
secuencia = secuencia_aleatoria(25, p)
print(secuencia)

### Escribir en un archivo y sin numpy
def seq_aleatorias(tamano = 100, p = [0.5, 0.5, 0.5, 0.5], seed = None,
                   num_seq = 10, archivo = "files/SeqAleatorias.fasta"):
    #Escribir en un archivo
    with open(archivo, 'w') as file:
        for i in range(num_seq):
            sec = secuencia_aleatoria(tamano, p, seed)
            file.write(">Seq" + str(i) + "\n")
            file.write(str(sec))
            file.write("\n")
    file.close()

### Trabajar con secuencias fasta u csv
from Bio import SeqIO
import csv
import re
#funcion para busqueda de patrones en archivo fasta
def busqueda_patron(fasta="files/SeqAleatorias.fasta", output="files/ejercicioNP.csv"):
    tf_interes_mod = {"TF_1": 'ATG[GG|TAG]', "TF_2": 'T[TC|AA]GAAT',
                      "TF_3": "GTATGCGGGG", "TF_4": "TAT[GT]CC",
                      "TF_5": "TATATA[GT|TG]"}
    outfile = open(output, "w")
    writer = csv.writer(outfile)
    for rec in SeqIO.parse(fasta, "fasta"):
        # secuencia por analizar
        seq = rec.seq
        # array para guardar numero de coindicencias
        tf_counts = np.empty((0), dtype="int")
        for tf in tf_interes_mod.values():
            counts = len(re.findall(tf, str(seq)))
            tf_counts = np.append(tf_counts, [counts])
        # escribir counts encontrados (iterable)
        writer.writerows([tf_counts])
    outfile.close()

### Matrices y graficas
###
#generar fasta con 10 secuencias distribucion p

seq_aleatorias(p = [0.3, 0.2, 0.3, 0.2])

# busqueda de patrones
busqueda_patron()

# matriz de cuentas
count_matrix =np.loadtxt("files/ejercicioNP.csv", delimiter=",", dtype = "int")
print(count_matrix)


# suma de los ejes 0
print(np.sum(count_matrix, axis = 0))
# suma del eje 1
print(np.sum(count_matrix, axis = 1))

# matriz binaria (1 y 0)
matrix_uno = np.where(count_matrix > 0, 1, 0 )

# multiplicacion de matrices
coexpresion = np.matmul(matrix_uno.T, matrix_uno)
print(coexpresion)
# plot de matriz de coexistencia de TFs
plt.imshow(coexpresion)
plt.colorbar()
plt.show()
## Grafo de matriz coexpresion
G = nx.DiGraph(coexpresion)
nx.draw(G, node_size = 900,  with_labels=True)
plt.show()
