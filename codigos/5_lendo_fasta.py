# encoding:utf-8

from Bio import SeqIO

for i in SeqIO.parse('exemplo_fasta', 'fasta'):
	print i.id # imprime o cabeçalho
	print i.seq # imprime a sequência