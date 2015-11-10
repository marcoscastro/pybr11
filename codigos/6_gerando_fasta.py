# encoding:utf-8

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

registro = SeqRecord(Seq('ACTG'), id='python_brasil')
arq = open('arquivo.fasta', 'w')
SeqIO.write(registro, arq, 'fasta')
arq.close()