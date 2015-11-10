# encoding:utf-8

from Bio import SeqIO

SeqIO.convert('exemplo_genbank.gbk', 'genbank', \
				'exemplo_fasta.fasta', 'fasta')