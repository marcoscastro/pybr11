from Bio import SeqIO

for i in SeqIO.parse('exemplo_genbank.gbk', 'genbank'):
	print i.id
	print i.seq