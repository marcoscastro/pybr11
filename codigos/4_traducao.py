# encoding:utf-8

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

rna = Seq('GUGCCC', IUPAC.unambiguous_rna)
proteina = rna.translate()
print proteina

# tradução direta
dna = Seq('ATGCTA', IUPAC.unambiguous_dna)
prot_dna = dna.translate()
print prot_dna