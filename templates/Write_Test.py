with open('dna_sequences.txt', 'r') as reader:
    dna_seq = reader.readlines()
    reader.close()
with open('dna_sequences.txt', 'w') as writer:
    # writer.writelines(reversed(dog_breeds))
    for line in dna_seq:
        writer.write("> " + line[:5] + '\n' + line[8:].replace('"', "").replace("-", "").upper() + '\n')
    writer.close()
