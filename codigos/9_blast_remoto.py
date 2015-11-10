from Bio import SeqIO
from Bio.Blast import NCBIWWW

arq = SeqIO.read('exemplo_fasta', format='fasta')
print 'Buscando...'
result = NCBIWWW.qblast('blastn', 'nt', \
			arq.seq, format_type='Text')
print result.read()
print 'Fim!'