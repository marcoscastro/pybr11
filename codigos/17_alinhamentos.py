# encoding:utf-8

'''
	Exemplo módulo pairwise2
	Doc:
		http://biopython.org/DIST/docs/api/Bio.pairwise2-module.html
'''

from Bio.pairwise2 import *

'''
	alinhamento global
	1 ponto para match (caractere igual)
	nenhum ponto para mismatch ou gap
'''
print 'Alinhamentos globais:\n'
alignments = align.globalxx('ACCGT', 'ACG')
for a in alignments:
	print format_alignment(*a)

# match: 2, mismatch = -1, gap = -0.5, gap extend = -0.1
'''
alignments = align.globalms('ACCGT', 'ACG', 2, -1, -0.5, -0.1)
for a in alignments:
	print format_alignment(*a)
'''

print '\nAlinhamentos locais:\n'
# alinhamento local
alignments = align.localxx('ACCGT', 'CCG')
for a in alignments:
	print format_alignment(*a)