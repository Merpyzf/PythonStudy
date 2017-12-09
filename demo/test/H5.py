# coding: UTF-8
import Bio.Alphabet
import os
from Bio import SeqIO
from Bio.SeqUtils import GC
import math
import numpy as np
import csv
import pickle
import re

list1 = ['A', 'T', 'C', 'G']
list2 = ['A', 'T', 'C', 'G']
list3 = ['A', 'T', 'C', 'G']
list4 = ['A', 'T', 'C', 'G']
list5 = ['A', 'T', 'C', 'G']

kmer_5 = list()
def get_base_pairs():
    """
    获取5个相邻碱基的所有的排列方式
    :return:
    """
    base_pairs = []
    for i in list1:
        for j in list2:
            for k in list3:
                for a in list4:
                    for b in list5:
                        base_pairs.append("".join([i, j, k, a, b]))
    return base_pairs


base_pairs = get_base_pairs()

print base_pairs.__len__()

seqs = SeqIO.parse("/Users/wangke/PycharmProjects/PythonStudy/demo/test/lncipedia_3_1_hc.fasta", "fasta")

count = 0

# 存放最后匹配的结果
result = []
for record in seqs:
    # 统计每块数据中碱排列的个数
    cell = {}
    # 存放
    lk5 = list()
    baseseq = record.seq
    # print baseseq
    print "----------"+"已经匹配的序列个数"+str(count)+"--------------"
    length = len(baseseq)
    n = 0
    for s in range(0, length - 4):
        if baseseq[s:s + 5] in base_pairs:
            n = n + 1
            key = str(baseseq[s:s + 5])
            if key in cell.keys():
                cell[key] = cell[key]+1
            else:
                cell[key] = 1
            # print('匹配到->' +str(count)+ baseseq[s:s + 5])
    count = count+1
    result.append(cell)
    print (result)



# kmer = np.hstack((H2.kmer_2, H3.kmer_3, kmer_5))



with open("mrna.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # writer.writerows(kmer)
csvfile.close()
