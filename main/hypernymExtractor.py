#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from __future__ import print_function
from util import read_file
from tqdm import tqdm
import codecs

SOURCE_FILE = r'umls_rrf/MRREL.RRF'
TARGE_FILE = r'data/hypernym_code.txt'

def extract_code():
	before = ''
	temp = []
	relation = []
	line_num = 0
	with codecs.open(SOURCE_FILE, encoding='utf-8') as f:
		for line in f:
			line_num += 1
			if line_num % 10000 == 0:
				print(line_num)
			k = line.split('|')
			if not k[0] == before:
				temp = []
			if k[3] == 'PAR':
				if [k[0], k[4]] not in temp:
					temp.append([k[0], k[4]])
					relation.append(k[0] + ' ' + k[4] + '\n')
				else:
					# print("已存在")
					continue
			before = k[0]

	with codecs.open(TARGE_FILE, 'w', encoding='utf-8') as ff:
		for line in relation:
			ff.write(line)

def extract_hyper():
	SOURCE_FILE = r'data/synsets.txt'
	TARGE_FILE = r'data/hypernym_code.txt'
	hyper_file = r'data/hypernym.txt'

	line_num = 0
	m1 = dict()
	temp = []
	with codecs.open(SOURCE_FILE, encoding='utf-8') as f:
		for line in f:
			line_num += 1
			if line_num % 10000 == 0:
				print(line_num)
			k = line.split('\t')
			m1[k[0]] = line_num

	with codecs.open(TARGE_FILE, encoding='utf-8') as f:
		for line in f:
			kk = line.strip().split(' ')
			num1 = m1.get(kk[0])
			num2 = m1.get(kk[1].replace('\n', ''))
			if num1 and num2:
				temp.append(str(num1) + ' ' + str(num2) + '\n')
			else:
				# 只要有一个为None
				continue

	with codecs.open(hyper_file, 'w', encoding='utf-8') as f:
		for line in temp:
			f.write(line)


if __name__ == '__main__':
	extract_code()
	extract_hyper()