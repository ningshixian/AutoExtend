#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=utf-8
import util
from tqdm import tqdm
import codecs

'''
	不同实体同名 集合抽取
'''

SYNSET_FILE = 'data/synsets.txt'
HOMONYM_FILE = r'data/homonym.txt'

syn_dic = dict()
homonym_dic = dict()
synsets = util.read_file(SYNSET_FILE)
for i in tqdm(range(len(synsets))):
	line = synsets[i]
	value = line.strip().split('\t')[0]
	array = line.strip().split('\t')[1]
	words = array.split('|')
	for word in words:
		if word not in syn_dic:
			syn_dic[word] = value
		else:
			vec = homonym_dic.get(word)
			if vec is None:
				homonym_dic[word] = [syn_dic[word],value]
			else:
				homonym_dic[word] = vec + [syn_dic[word], value]
print(len(homonym_dic))


with codecs.open(HOMONYM_FILE,'w',encoding='utf-8') as f:
	for key in homonym_dic.keys():
		line = key + ':' + '|'.join(homonym_dic[key])
		f.write(line)
		f.write('\n')



