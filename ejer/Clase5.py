from Bio.Seq import Seq
from Bio.SeqUtils import nt_search
print("Dame la secuencia donde sospechas que hay un ORF")
secuencia = Seq(input())
c_inicio = Seq("ATG")
c_final = Seq("TGA")
inicio = nt_search(str(secuencia), c_inicio)
print(inicio)

for i in range(1, len(inicio)):
    sec_prot = secuencia[i:]
    proteina = sec_prot.translate(to_stop=True)
    print(proteina)