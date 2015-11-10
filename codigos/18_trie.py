# encoding:utf-8

'''
Exemplo Árvore Trie

Referências:
	http://biopython.org/DIST/docs/api/Bio.trie-module.html
	http://biopython.org/DIST/docs/api/Bio.triefind-module.html
	https://www.youtube.com/watch?v=9U0ynguwoNA
	http://bioinformatics.cvr.ac.uk/blog/trie-data-structure/
'''

from Bio.trie import trie
from Bio import triefind

t = trie()

# conjunto de palavras
seqs = ['AAAA', 'ACGT', 'CGA',\
		'GTA', 'TA', 'TTTT']

# adiciona as chaves
for seq in seqs:
	t[seq] = None

# imprime as chaves com determinado prefixo
print t.with_prefix('A')

genome = 'ACGTA'

# encontra todas as chaves em qualquer lugar da string
print triefind.find(genome, t)

# encontra a mais longa chave a partir do início da string
print triefind.match(genome, t)