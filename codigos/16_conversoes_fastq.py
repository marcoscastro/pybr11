# encoding:utf-8

# conversões FASTQ -> FASTA

from Bio import SeqIO

# FASTQ -> FASTA
SeqIO.convert('exemplo.fastq', 'fastq',\
				'exemplo.fasta', 'fasta')

# FASTQ -> QUAL
SeqIO.convert('exemplo.fastq', 'fastq',\
				'exemplo.qual', 'qual')