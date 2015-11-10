# encoding:utf-8

# manipulando arquivos PDB
# download do arquivo: www.rcsb.org/pdb/files/1bga.pdb

from Bio.PDB import *

# cria um objeto PDBParser
parser = PDBParser()

# nome da estrutura e o arquivo PDB
estrutura = parser.get_structure('BGA', '1bga.pdb')

# obtendo a informação de cabeçalho
cabecalho = parser.get_header()

print cabecalho