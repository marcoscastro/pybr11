# encoding:utf-8

'''
Recebendo um arquivo Multi-FASTA e
ordenar as sequências pelo tamanho
'''

from Bio import SeqIO

seqs = list(SeqIO.parse('multifasta.txt', 'fasta'))
seqs.sort(cmp=lambda x,y: cmp(len(x), len(y)))
SeqIO.write(seqs, 'multifasta_sorted.txt', 'fasta')