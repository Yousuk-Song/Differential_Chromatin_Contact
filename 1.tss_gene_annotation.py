#!/data2/home/song7602/miniconda3/bin/python3.11

import sys

coo = sys.argv[1]

gene_pos_dict = {}
n = 0
#pos_file = open(f'{sys.path[0]}/Gencode_Protein_Coding_POS_list.txt', 'r')

pos_file = open(f'{sys.path[0]}/gencode_protein_coding_gene.hg38.tsv', 'r')
#chr22   20779313        20780201        +       SERPIND1

for line in pos_file:
	if n == 0:
		n = 1
		continue
	cols = line.rstrip().split()
	chrom = cols[0]
	start = int(cols[1])
	end = int(cols[2])
	strand = cols[3]
	gene = cols[4]
	gene_pos_dict[(chrom, start, end, strand)] = gene
pos_file.close()

padding=1000
tss_count_dict = {}
for line in open(coo):
	cols = line.rstrip().split('\t')
	chr1 = cols[0]
	pos1_1 = int(cols[1])
	pos1_2 = int(cols[2])
	chr2 = cols[3]
	pos2_1 = int(cols[4])
	pos2_2 = int(cols[5])
	count = int(cols[6])
	if chr1 == chr2:
		if abs(pos1_1 - pos2_2) < 1000000:
			for gene_pos in gene_pos_dict:
				gene_chrom = gene_pos[0]
				gene_strand = gene_pos[3]
				if gene_strand == '+':
					tss = gene_pos[1]
				elif gene_strand == '-':
					tss = gene_pos[2]
				if chr1 == gene_chrom:
					if pos1_1 - padding <= tss <= pos1_2 + padding:
						gene = gene_pos_dict[gene_pos]
						if gene not in tss_count_dict:
							tss_count_dict[gene] = [count]
						else:
							tss_count_dict[gene].append(count)
	del line

for gene in tss_count_dict:
	tss_count_dict[gene] = max(tss_count_dict[gene])

fo = open(coo.split('/')[-1].replace('.tsv', '.gene_count.csv'), 'w')
fo.write(f'Gene,Count\n')
for gene in tss_count_dict:
	fo.write(f'{gene},{tss_count_dict[gene]}\n')
fo.close()










