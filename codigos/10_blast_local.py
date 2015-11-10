# encoding:utf-8

# executando o blast localmente
# download: ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST

# comparando duas sequências de nucleotídeos

from Bio.Blast.Applications import *

comando = NcbiblastnCommandline(
				query='seq1.fasta', subject='seq2.fasta',
				outfmt=0, out='saida.txt')
stdout, stderr = comando()
result = open('saida.txt', 'r')
print result.read()