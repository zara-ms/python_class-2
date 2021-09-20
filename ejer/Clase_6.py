from Bio import SeqIO
from Bio.Seq import Seq

# path = "../src/sample.fastq"
path = 'sample.fastq'
mala_calidad = []
umbral = 32
for record in SeqIO.parse(path, "fastq"):
    promedio = sum(record.letter_annotations["phred_quality"])/len(record.letter_annotations["phred_quality"])
    if promedio < umbral:
        mala_calidad.append((promedio, record.id))

print(len(mala_calidad))
