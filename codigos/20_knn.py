# encoding:utf-8

'''
	Example kNN - k-nearest-neighbors classification
	Doc: http://pydoc.net/Python/biopython/1.63/Bio.kNN/
	Needs numpy package
'''

from Bio import kNN

# list of the neighbors
xs = [
		[10, 10, 10, 10], [9, 11, 10, 10],
		[10, 10, 11, 9], [25, 5, 5, 5],
		[9, 9, 11, 11], [15, 15, 5, 5],
		[5, 10, 5, 20], [9, 9, 9, 13],
		[9, 11, 11, 9], [20, 10, 5, 5],
		[9, 10, 11, 10], [5, 15, 15, 5]
	]

# list of the classes that the neighbors belong to
ys = [1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

# number of neighbors to look at
k = 3

# training...
knn = kNN.train(xs, ys, k)

# testing...
new_example = [5, 25, 5, 5]
print kNN.classify(knn, new_example)