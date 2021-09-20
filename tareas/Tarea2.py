from Bio import SeqIO

def resumen(in_path, genes):
    # With SeqIO we parse the path for the desired file
    for gb_record in SeqIO.parse(in_path, "genbank"):
        # Both organism and version are held in annotations
        print('Organism:', gb_record.annotations['organism'])
        print('Version:', gb_record.annotations['sequence_version'])
        # As for isolated source and country, it is needed to acces to quialifers in features
        print('Isolated:', gb_record.features[0].qualifiers['isolation_source'])
        print('Country:', gb_record.features[0].qualifiers['country'])

        # In this new for, the next section of qualifiers is accessed
    for record in SeqIO.parse(in_path, "genbank"):
        print('name gene', record.features[2].qualifiers)
        # First will help us to determine the start location of the desired sequence
        first = record.features[1].location.start
        print('DNA:', record.seq[first:15])
        print('RNA:', record.seq.transcribe(record.seq[first:15]))
        # Since the 15 aminoacids are codified by 3 units each, the end shall be 3x15
        print('amin:',record.translate(record.seq[first:45]) )

search=['N']

resumen("virus.gb", search)
