#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from __future__ import print_function
from collections import OrderedDict
import util
import numpy as np
from tqdm import tqdm
import codecs

SYNSETS_FILE = r'data/synsets.txt'
LEXEMES_FILE = r'data/lexemes.txt'


def extract_lexemes(source, targe):
	'''
	抽取结果 数值化 （文件较小）
	'''
	print("Starting...")

	map = OrderedDict()
	lexemes = []
	sets = []
	line_num = 1
	wn = 0  # 词对应的编号

	content = util.read_file(source)
	for i in tqdm(range(len(content))):
		line = content[i]
		array = line.strip().split('\t')
		cui = array[0]
		words = array[1].split('|')[:-1] # 去掉最后一个['']
		for word in words:
			if word not in map:
				wn += 1
				map[word] = wn
				lexemes.append(wn)
				sets.append(line_num)
			else:
				num = map[word]
				lexemes.append(num)
				sets.append(line_num)
		line_num += 1

	with codecs.open(targe, 'w', encoding='utf-8') as file:
		for i in tqdm(range(len(lexemes))):
			file.write(str(lexemes[i]) + ' ' + str(sets[i]) + '\n')

if __name__ == '__main__':
	extract_lexemes(SYNSETS_FILE, LEXEMES_FILE)
