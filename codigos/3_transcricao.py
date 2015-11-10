from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

dna = Seq('ACTG', IUPAC.unambiguous_dna)
rna = dna.transcribe()
print rna # imprime ACUG
print rna.back_transcribe() # imprime ACTG