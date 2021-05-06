file = open("4_dna_sequences.txt")
all_lines = file.readlines()
for line in all_lines:
  print("> " + line[:5] + '\n' + line[8:].replace('"', "").replace("-", "").upper())
file.close()
