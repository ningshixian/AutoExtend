#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from __future__ import print_function
import numpy as np
from tqdm import tqdm
import codecs
import pickle


def is_terminator(ch):
	return ch in (u'!', u'?', u',', u';', u'.', u'！', u'？', u'，', u'。', u'…')


def read_file(path):
	content = []
	with codecs.open(path) as f:
		for line in f:
			content.append(line.strip())
	return content


# how much lines in a very big file?
def count_lines(file2):
	row = 0
	with open(file2) as f:
		while True:
			line = f.readline()
			if not line: break
			row += 1
		return row


def readEmbedFile(GLOVE_FILE):
	'''
		读词向量文件
	'''
	print("读取词向量文件中...")

	embeddings_index = dict()
	line_num = 0
	# 文件无法被装载在内存中发生溢出了
	with codecs.open(GLOVE_FILE, encoding='utf-8') as f:
		for line in f:
			line_num += 1
			if line_num % 10000 == 0:
				print(line_num)
			# if line_num == 1:
			# 	continue
			values = line.strip().split()
			word = values[0]
			embedding = ' '.join(values[1:])  # 把list转换为字符串
			embeddings_index[word] = embedding
	print('读取完毕, 共%d行' % len(embeddings_index))

	# with open('embedding100.pkl', 'wb') as output:
	# 	pickle.dump(embeddings_index, output, True)

	return embeddings_index


def count_diff(GLOVE_FILE, FILE):
	map = readEmbedFile(GLOVE_FILE)

	num_notin = 0
	total = 0
	temp = dict()
	lines = []
	with open(FILE, 'r') as f:
		for line in f:
			lines.append(line)
	for i in tqdm(range(len(lines))):
		line = lines[i]
		word = line.split()[1:]
		for one in word:
			if one not in temp.keys():
				temp[one] = None
				total += 1
				if one not in map.keys():
					num_notin += 1
	print('\n' + '同义词词林中词的总个数：' + str(total))  # 77456
	print('\n' + '在词林但不在词向量中的词的个数：' + str(num_notin))  # 9857


def test_vectors(file):
	'''用于测试词向量文件中含有的无法解码的行'''
	with open(file) as f:
		row = 1
		try:
			for line in f:
				row += 1
		except:
			print('--------------------' + str(row))


if __name__ == '__main__':
	# count_diff('data/vectors.txt', 'data/TongyiciCilin.txt')
	# test_vectors('data/synsets.txt')

	temp =''
	arr =list(np.random.uniform(-1,1,100).round(6))
	print(i for i in arr)