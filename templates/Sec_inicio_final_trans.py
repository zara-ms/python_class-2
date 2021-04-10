
rna = "AAGGAUGUCGCGCGUUAUUAGCCUAA"
inicio = rna.find("AUG")
final = rna.find("UAA")
print("El codon de inicio empieza en posicion: ", inicio)
print("Y la secuencia transcrita termina en :", final+3)
print("La secuencia transcrita es :", rna[inicio:final+3])
'''NAME
	Sec_inicio_final_trans.py

VERSION
	1.0

AUTHOR
	Rodel-OL

DESCRIPTION
	Programa para saber donde inicia un transcrito de RNA, donde termina, y que secuencia transcribe.
	El final de paro se le aumentan 3 unidades al momento de sacar resutado para que este incluido el triplete mencionado

CATEGORY
	

USAGE
	

ARGUMENTS


INPUT
	rna, secuencia de RNA

OUTPUT
	inicio de la transcripcion
	final de la transcripcion
	secuencia transcrita

'''