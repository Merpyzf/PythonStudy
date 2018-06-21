# coding: UTF-8
import Bio.Alphabet
import os
from Bio import SeqIO
from Bio.SeqUtils import GC
import math
import numpy
import csv
import pickle
import re


##########################################################################
########################      H3
list1=['A','T','C','G']
list2=['A','T','C','G']
list3=['A','T','C','G']
kmer_3=list()
for record in SeqIO.parse("E:\\pycode\\seq\\gencode.v26.pc_transcripts.fasta","fasta"):
    lk3=list()
    baseseq=record.seq
    L=len(baseseq)
    #print(baseseq)
    #print (L)
    for i in list1:
        for j in list2:
            for k in list3:
                p=0
                n=0
                hp=0
                basestr="".join([i,j,k])
                for s in range(0,L-2):
                    if baseseq[s:s+3]==basestr:
                        n=n+1
                #print(n)
                """
                p=float(n)/L
                if p!=0:
                    hp=p*math.log(p,2)
                    H3=H3+hp
                """
                lk3.append(n)
    kmer_3.append(lk3)









                    
            
            
