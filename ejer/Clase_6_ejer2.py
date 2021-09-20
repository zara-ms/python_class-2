from Bio import SeqIO

for gb_record in SeqIO.parse("../src/aichi.gb", "genbank"):
    print('ID', gb_record.id)
    print('secuencia', str(gb_record.seq)[0:30], '...')
    print('Longitud', len(gb_record))

for gb_record in SeqIO.parse("../src/virus.gb", "genbank"):
    print('ID', gb_record.id)
    print(gb_record.annotations)
    version = gb_record.annotations['sequence_version']
    organismo = gb_record.annotations['organism']
    print(version, organismo)

path = "../src/virus.gb"
for gb_record in SeqIO.parse(path, "genbank"):
    print('ID', gb_record.id)
    #features
    fuente_aislado = gb_record.features[0].qualifiers["isolation_source"]
    pais = gb_record.features[0].qualifiers["country"]
    print(fuente_aislado, pais)
