#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from __future__ import print_function
from util import read_file
from tqdm import tqdm
import codecs

SOURCE_FILE = r'umls_rrf/MRCONSO_new.RRF'
TARGE_FILE = r'data/synsets.txt'

before = ''
temp_line = ''
temp = []
# 一次性读取 MRCONSO 概念文件   (synsets 第一行丢失部分)
content = read_file(SOURCE_FILE)
for i in tqdm(range(len(content))):
	line = content[i]
	splited_line = line.split('|')
	cui = splited_line[0]
	string = splited_line[14]
	if cui != before:
		temp.append(temp_line)
		temp_line = cui + '\t'
	temp_line += string.replace(' ', '_')+'|'
	before = cui
temp.append(temp_line)

with codecs.open(TARGE_FILE, 'w', encoding='utf-8') as f:
	for line in temp:
		f.write(line)
		f.write('\n')