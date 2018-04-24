#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding=utf-8

from __future__ import print_function
from tqdm import tqdm
import util
import numpy as np
import codecs
import pickle

GLOVE_FILE = r'embedding/embedding100.vec'
SYNSET_FILE = 'data/synsets.txt'
WORD_FILE = r'data/words.txt'


def new_wordVector(GLOVE_FILE, SYNSET_FILE, WORD_FILE):
	print("Starting....")

	# emb_dict = util.readEmbedFile(GLOVE_FILE)
	with open(r'embedding/embedding100.pkl','rb') as f:  # python2 64 bit 执行
		emb_dict = pickle.load(f)

	uni_word = dict()
	temp = []
	number = 0  # 未登录词数量
	total = 0
	index = 1   # 字典索引

	synsets = util.read_file(SYNSET_FILE)

	for i in tqdm(range(len(synsets))):
		line = synsets[i]
		array = line.strip().split('\t')[1]
		words = array.split('|')
		for word in words:
			if word not in uni_word:  # 多个相同词向量仅保留一个
				uni_word[word] = index  # list 有频繁插入,换成dict
				index += 1
				if word in emb_dict:  # 保留即在词林，又在词向量文件中的词
					vec = emb_dict[word]
					if ' ' in word: print('have ')
					temp.append(word + ' ' + vec + '\n')
				else:
					number += 1
					arr = np.random.uniform(-0.5, 0.5, 100).round(6) # 未登录词 随机初始化
					vec = ''
					for dim in arr:
						vec += str(dim) + ' '
					vec = vec.strip() + '\n'
					if ' ' in word: print('have ')
					temp.append(word + ' ' + vec)
			else:continue


	with codecs.open(WORD_FILE, 'w', encoding='utf-8') as word_file:
		for line in temp:
			word_file.write(line)

	print('未登录词数量: %d' % number)  # 334501
	print('总共: %d' % index)  # 367032
	print('重新生成词向量文件 %s 完成' %WORD_FILE)


if __name__ == '__main__':
	new_wordVector(GLOVE_FILE, SYNSET_FILE, WORD_FILE)
