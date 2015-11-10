# encoding:utf-8


'''
	Esse arquivo necessita do módulo pylab
	Pode-se instalar matplotlib: pip install matplotlib
'''

from Bio.Seq import Seq
from Bio.SeqUtils import GC
import pylab

# conteúdo GC: quantidade de bases di DNA que são guanina ou citosina
# esse código mostra a porcentagem de conteúdo GC em forma de pizza

seq = Seq('CTTGCACTGACATCGAT')
gc = GC(seq)
at = 100 - gc

pylab.pie([gc, at]) # criado o gráfico de pizza
pylab.title('GC Content') # adiciona um título
pylab.xlabel('GC: %0.1f\nAT: %0.1f' % (gc, at)) # porcentagens
pylab.show() # mostra o gráfico