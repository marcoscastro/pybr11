# encoding:utf-8


'''
	Esse arquivo necessita do módulo pylab
	Pode-se instalar matplotlib: pip install matplotlib
'''

from Bio import SeqIO
import pylab

# leitura de algum genoma
arq = SeqIO.read('NC_017108.gbk', 'genbank')

'''
	lista com os tamanhos das sequências codificantes
	CDS: coding sequence (sequência codificante) ou ORF (quadro aberto de leitura)
	a sequência codificante é uma sequência de aminoácidos
	na sua cadeia, o gene possui uma região chamada de região codificadora
	de proteínas que é onde estão os nucleotídeos que propriamente darão origem
	ao RNA através do processo de transcrição e consequentemente às proteinas
'''
tamanhos = [len(i.qualifiers['translation'][0]) \
			for i in arq.features if i.type == 'CDS']

# mostra a quantidade de genes pelo tamanho da sequência codificadora

# hist recebe a lista dos tamanhos, bins é a quantidade de barras do histograma
pylab.hist(tamanhos, bins=20)
pylab.title('Frequencia de sequencias') # define o título
pylab.xlabel('Tamanho da sequencia (bp)') # define o título do eixo X
pylab.ylabel('Quantidade') # define o título do eixo Y
pylab.show() # mostra a imagem