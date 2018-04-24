#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
对 MRCONSO 文件预处理(过滤)
'''
import codecs
from tqdm import tqdm

base = r'umls_rrf/'
MRCONSO_FILE = base + 'MRCONSO.RRF'
MRSTY_FILE = base + 'MRSTY.RRF'
MRCONSO_PN_FILE = base + 'MRCONSO_new.RRF'
ProteinDic = base + 'ProteinDic.txt'


# 1 MRCONSO( 仅保留 MSH+ENG )
def extractCONSO():
    line_num = 0
    conso = []
    cuiSet = set()
    with codecs.open(MRCONSO_FILE, encoding='utf-8') as f:
        while True:
            line = f.readline()
            if line_num % 10000 == 0:
                print(line_num)
            line_num += 1
            if not line: break
            splited_line = line.strip().split('|')
            if splited_line[1] == 'ENG':
                if splited_line[11] == 'MSH':
                    conso.append(line)
                    cuiSet.add(splited_line[0])

    # 2 选取 MRSTY 中的蛋白质 - MSH+ENG的类别
    mrsty = []
    cuiSet_new = set()
    cd = [
        'Clinical Drug', 'Organic Chemical',
        'Inorganic Chemical', 'Disease or Syndrome'
    ]
    ppi = ['Amino Acid, Peptide, or Protein', 'Gene or Genome']
    with codecs.open(MRSTY_FILE, 'r', 'utf-8') as f:
        for line in f:
            splited_line = line.strip().split('|')
            if splited_line[3] in ppi and splited_line[0] in cuiSet:
                mrsty.append(splited_line[0] + '|' + splited_line[3] + '\n')  # CUI | TYPE
                cuiSet_new.add(splited_line[0])

    # 3 通过 MRSTY 筛选出 MRCONSO 中蛋白质-相关的类别
    temp = []
    for line in conso:
        splited_line = line.strip().split('|')
        cui = splited_line[0]
        if cui in cuiSet_new:
            temp.append(line)

    with codecs.open(MRCONSO_PN_FILE, 'w', encoding='utf-8') as f:
        for line in temp:
            f.write(line)


if __name__ == '__main__':
    # extractCONSO()

    with codecs.open(MRCONSO_PN_FILE, 'r', encoding='utf-8') as f:
        with codecs.open(ProteinDic, 'w', encoding='utf-8') as p:
            for line in f:
                string = line.strip().split('|')[14]
                p.write(string)
                p.write('\n')
                # if 'Protein' in string:
                #     p.write(string.replace('Protein','').strip())
                #     p.write('\n')