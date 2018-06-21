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

##########################
'''
#fh = open("E:\\pycode\\csvtest.csv")
mylist = list(csv.reader(open('csvtest.csv')))
#myset=set(mylist)
n=2
seq1=mylist[2][1]
l=len(seq1)
#print(seq1)
for i in range(0,len(seq1)-2):
    str1=str(seq1[i:i+2])
    list1=list(str1)
    #list2=list.append (list1)
    print (list1)
'''
########################################
###########   H2
list1 = ['A', 'T', 'C', 'G']
list2 = ['A', 'T', 'C', 'G']

kmer_2 = list()
# csvFile2 = open("E:\\pycode\\data\\test\\test.csv",'w', newline='')#####设置newline，否则两行之间会空一行
# writer = csv.writer(csvFile2)
for record in SeqIO.parse("E:\\pycode\\seq\\gencode.v26.pc_transcripts.fasta", "fasta"):
    lk2 = list()
    baseseq = record.seq
    L = len(baseseq)
    num1 = 0  # 列
    for i in list1:
        for j in list2:
            p = 0
            n = 0
            basestr = "".join([i, j])
            for s in range(0, L - 1):
                if baseseq[s:s + 2] == basestr:
                    n = n + 1  ############    统计数量   ############
                    # print(n)
                    ##################   熵计算####################
            """
            p=float(n)/L
            if p!=0:
                hp=p*math.log(p,2)
                #H2=H2+hp
            else:
                hp=0
            """
            lk2.append(n)
    kmer_2.append(lk2)








#####
