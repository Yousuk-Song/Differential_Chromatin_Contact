#!/data2/home/song7602/miniconda3/bin/python3.11

import sys

n_1_count = 'SRR1658693.Normal.chr9-chr22.Raw.mcool_25kb_contacts.raw_values.ginteractions.gene_count.normalized.csv' #sys.argv[1] # normal SRR1658693
n_2_count = 'SRR1658694.Normal.chr9-chr22.Raw.mcool_25kb_contacts.raw_values.ginteractions.gene_count.normalized.csv' # sys.argv[2] # normal SRR1658693
p_1_count = 'SRR1658693.Philadelphia.chr9-chr22.Raw.mcool_25kb_contacts.raw_values.ginteractions.gene_count.normalized.csv' #sys.argv[3] # philadelphia SRR1658694
p_2_count = 'SRR1658694.Philadelphia.chr9-chr22.Raw.mcool_25kb_contacts.raw_values.ginteractions.gene_count.normalized.csv' #sys.argv[4] # philadelphia SRR1658694

N_1_dict = {}
n = 0 
for line in open(n_1_count):
	cols = line.rstrip().split(',')
	if n == 0:
		n = 1 
		continue
	gene = cols[0]
	count = cols[1]	
	N_1_dict[gene] = count

N_2_dict = {}
n = 0 
for line in open(n_2_count):
	cols = line.rstrip().split(',')
	if n == 0:
		n = 1
		continue
	gene = cols[0]
	count = cols[1]
	N_2_dict[gene] = count

P_1_dict = {}
n = 0
for line in open(p_1_count):
	if n == 0:
		n = 1 
		continue
	cols = line.rstrip().split(',')
	gene = cols[0]
	count = cols[1]	
	P_1_dict[gene] = count

P_2_dict = {}
n = 0
for line in open(p_1_count):
	if n == 0:
		n = 1
		continue
	cols = line.rstrip().split(',')
	gene = cols[0]
	count = cols[1]
	P_2_dict[gene] = count

common_gene = sorted(list(set([gene for gene in N_1_dict if gene in N_2_dict and gene in P_1_dict and gene in P_2_dict])))

fo = open('Chromatin_Contact.Normal-Philadelphia.merged.csv', 'w')
fo.write('Gene,SRR1658693-N,SRR1658694-N,SRR1658693-P,SRR1658694-P\n')
for gene in common_gene:
	fo.write(f'{gene},{N_1_dict[gene]},{N_2_dict[gene]},{P_1_dict[gene]},{P_2_dict[gene]}\n')
fo.close()





