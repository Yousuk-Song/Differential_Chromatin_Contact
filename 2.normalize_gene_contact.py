#!/data2/home/song7602/miniconda3/bin/python3.11

import sys
import pysam

bam = sys.argv[1]
contact = sys.argv[2]

# coverage
samfile = pysam.AlignmentFile(bam, "rb")

coverage_list = []
for pileupcolumn in samfile.pileup():
	coverage_list.append(pileupcolumn.n)

average_coverage = sum(coverage_list) / len(coverage_list)
samfile.close()

# read numb 
samfile = pysam.AlignmentFile(bam, "rb")
read_numb = 0
for read in samfile:
	read_numb += 1
samfile.close()

# normalize
#average_coverage = 1
fo = open(contact.replace('.csv', '.normalized.csv'), 'w')
fo.write('Gene,Count\n')
n = 0
for line in open(contact):
	if n == 0:
		n = 1
		continue
	cols = line.rstrip().split(',')
	gene = cols[0]
	count = int(cols[1])
	adjusted_count = round(1000000*(count/(read_numb * average_coverage)), 3)
	fo.write(f'{gene},{adjusted_count}\n')
fo.close()





