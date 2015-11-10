# encoding:utf-8

'''
Calculando o N50 de um arquivo Multi-FASTA
N50 é uma métrica usada para avaliar montagens de genomas.
'''

from Bio import SeqIO

# obtém as sequências do arquivo
seqs = list(SeqIO.parse('multifasta.txt', 'fasta'))

# obtém os tamanhos das sequências
tamanhos = [len(seq) for seq in seqs]

tamanhos.sort() # ordena crescentemente
metade = sum(tamanhos) / 2 # obtém a metade
soma_tamanhos = 0 # acumula os tamanhos

# detecta o N50
for tam in tamanhos:
	soma_tamanhos += tam
	if soma_tamanhos > metade:
		print 'N50: %s' % tam
		break