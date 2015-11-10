# encoding:utf-8

'''
	Example Genetic Algorithm using BioPython
	Documentation:
		http://biopython.org/DIST/docs/api/Bio.GA-module.html
'''

from random import randint
from Bio.Alphabet import IUPAC
from Bio.Seq import MutableSeq
from Bio.GA.Organism import Organism
from Bio.GA.Crossover.Point import SinglePointCrossover
from Bio.GA.Mutation.Simple import SinglePositionMutation
from Bio.GA.Selection.RouletteWheel import RouletteWheelSelection

def show_pop(pop):
	for p in pop:
		print p

# GC content
def fitness(s):
	return (s.count('G') + s.count('C'))

# GA parameters
pop_size, seq_size, max_gen = 20, 10, 1000
cross_rate, mut_cross = 0.8, 0.1
pop = []

# chooses a random base
def random_base():
	return ('ACTG')[randint(0,3)]

# generates individuals
for i in range(pop_size):
	seq = MutableSeq(''.join(\
			random_base() for j in range(seq_size)),\
			IUPAC.unambiguous_dna)
	pop.append(Organism(seq, fitness))

cross = SinglePointCrossover(cross_rate)
mut = SinglePositionMutation(mut_cross)
roulette = RouletteWheelSelection(mut, cross)

for i in range(max_gen):
	pop = roulette.select(pop)
	for j in range(pop_size):
		pop[j].fitness = fitness(pop[j].genome)

show_pop(pop)