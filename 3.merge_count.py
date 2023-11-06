#!/data2/home/song7602/miniconda3/bin/python3.11

import sys

s1_a_count = sys.argv[1]
s2_a_count = sys.argv[2]
s1_b_count = sys.argv[3]
s2_b_count = sys.argv[4]
chrom = sys.argv[5]

s1_A_dict = {}
n = 0 
for line in open(s1_a_count):
	cols = line.rstrip().split(',')
	if n == 0:
		n = 1 
		continue
	gene = cols[0]
	count = cols[1]	
	s1_A_dict[gene] = count

s2_A_dict = {}
n = 0
for line in open(s2_a_count):
	cols = line.rstrip().split(',')
	if n == 0:
		n = 1 
		continue
	gene = cols[0]
	count = cols[1]
	s2_A_dict[gene] = count


s1_B_dict = {}
n = 0
for line in open(s1_b_count):
	if n == 0:
		n = 1 
		continue
	cols = line.rstrip().split(',')
	gene = cols[0]
	count = cols[1]	
	s1_B_dict[gene] = count

s2_B_dict = {}
n = 0
for line in open(s2_b_count):
	if n == 0:
		n = 1
		continue
	cols = line.rstrip().split(',')
	gene = cols[0]
	count = cols[1]
	s2_B_dict[gene] = count

common_gene = [gene for gene in s1_A_dict if gene in s2_A_dict if gene in s1_B_dict if gene in s2_B_dict]

fo = open(f'{chrom}.interaction.merged.count.csv', 'w')
fo.write('Gene,A_S1,A_S2,B_S1,B_S2\n')
for gene in common_gene:
	fo.write(f'{gene},{s1_A_dict[gene]},{s2_A_dict[gene]},{s1_B_dict[gene]},{s2_B_dict[gene]}\n')
fo.close()



