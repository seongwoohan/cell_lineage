import sys
import os
import numpy as np
import pandas as pd
#from Bio import SeqIO

# text file location
source = "/Users/seongwoohan/desktop/sra_data.fasta_cut.txt"


# Output of every possibility of gel_barcode1.txt and gel_barcode2.txt
def generate():
	gel1 = open("/Users/seongwoohan/Desktop/gel_barcode1.txt", "r")
	gel2 = open("/Users/seongwoohan/Desktop/gel_barcode2.txt", "r")

	lines1 = gel1.readlines()
	lines2 = gel2.readlines()
	for line1 in lines1:   
		for line2 in lines2:
			print(line1.strip() + '-' + line2.strip())

generate()


# Only read the line with head sequence
def head_sequence():
	source = "/Users/seongwoohan/desktop/sra_data.fasta_cut.txt"
	seq = open(source, "r")    
	fastaLines = seq.readlines()[::2]
	for line1 in fastaLines:
		print(line1.rstrip())



# Only read the line with gene sequence
def base_sequence():
	source = "/Users/seongwoohan/desktop/sra_data.fasta_cut.txt"
	seq = open(source, "r")    
	fastaLines = seq.readlines()
	count = 0
	for i in range(0, len(fastaLines)):
		count+=1
		if (i%2 != 0):
			print(str(count) + ' ' + (fastaLines[i]).rstrip())


# Checking if gel_barcode2.txt is in the fasta file
def fullBar():
	gel2 = open("/Users/seongwoohan/Desktop/gel_barcode2.txt", "r")
	seq = open("/Users/seongwoohan/desktop/sra_data.fasta_cut.txt", "r")    

	barcode = gel2.readlines()
	fastaLines = seq.readlines()[0::2]

	count = 0
	for line2 in barcode: 
		count +=1
		for line1 in fastaLines:
			if line2.rstrip() in line1:
				print(line1.split(':')[0] + ' corresponds to line #' + str(count) 
					+ ' in barcode2.txt: ' +line2.rstrip())

fullBar()

# Save unique head sequences into a list
def head_seq_list():
    source = "/Users/seongwoohan/desktop/sra_data.fasta_cut.txt"
    seq = open(source, "r")    
    fastaLines = seq.readlines()[::2]
    headList = []
    
    for line1 in fastaLines:
        num_head_seq = line1.split(':')[0].split(' ')[1]
        headList.append(num_head_seq)  
    #print(headList)
    return headList

head_seq_list()


# Save gene sequence into a list
def gene_seq_list():
    source = "/Users/seongwoohan/desktop/sra_data.fasta_cut.txt"
    seq = open(source, "r")   
	
    fastaLines = seq.readlines()
    geneList = []
    
    for i in range(0, len(fastaLines)):
        if (i%2 != 0):
            num_gene_seq = (fastaLines[i]).rstrip()
            geneList.append(num_gene_seq)
    #print(geneList) 
    return geneList
    
gene_seq_list()  


# Count how many each head sequence has gene sequence
def mapping():
    headList = head_seq_list()
    geneList = gene_seq_list()
	
    df = pd.DataFrame({'head':headList, 'gene':geneList}) 
    uniqueHeadList = df['head'].unique().tolist()
    
    for uniqueHead in uniqueHeadList:
        uniqueDF = df[df['head'] == uniqueHead]
        genes = uniqueDF['gene'].tolist()
        print('{0}:{1}, {1}'.format(uniqueHead, len(genes), genes))
        #print('{0}: {1}'.format(unique, genes))
        #print('{0}: {1}'.format(uniqueHead, genes))

mapping()

