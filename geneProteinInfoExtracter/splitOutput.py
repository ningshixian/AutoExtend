#!/usr/bin/python3
# -*- encoding: utf-8 -*-
from __future__ import print_function
from tqdm import tqdm
import util
import codecs

'''
用于将 OutputVectors.txt 文件分成 words\lexemes\synsets 三个文件
'''


OUTPUT = 'naive/outputVectors.txt'
WORDS_FILE = 'auto_output/words.txt'
SYNSETS_FILE = 'auto_output/synsets.txt'
LEXEMES_FILE = 'auto_output/lexemes.txt'
words = []
synsets = []
lexemes = []


def split_output(OUTPUT):
	line_num =0
	edge = 1000000
	lines = []
	with codecs.open(OUTPUT, 'r', 'utf-8') as f:
		for line in f:
			if line_num%10000==0:print(line_num)
			line_num += 1
			lines.append(line.strip())

	print(len(lines))	#7355

	for i in tqdm(range(len(lines))):
		line = lines[i]
		# print(i, line.split())
		first = line.split()[0]
		if '::,' not in first:
			if i<edge:
				words.append(line)
			else:
				lexemes.append(line)
		else:
			edge = i
			synsets.append(line)

	with codecs.open(WORDS_FILE, 'w', encoding='utf-8') as f:
		for i in tqdm(range(len(words))):
			f.write(words[i])
			f.write('\n')
	with codecs.open(SYNSETS_FILE, 'w', encoding='utf-8') as f:
		for i in tqdm(range(len(synsets))):
			f.write(synsets[i] + '\n')
	with codecs.open(LEXEMES_FILE, 'w', encoding='utf-8') as f:
		for i in tqdm(range(len(lexemes))):
			f.write(lexemes[i] + '\n')


if __name__ == '__main__':
	split_output(OUTPUT)

	# lexemes = {}
	# line_num = 0
	# with codecs.open('auto_output/lexemes.txt', 'r', 'utf-8') as f:
	# 	for line in f:
	# 		if line_num%10000==0:print(line_num)
	# 		line_num += 1
	# 		splited_line = line.split()
	# 		first = splited_line[0]
	# 		vector = line[len(first)+1:]
	# 		if first.endswith('-') or first.endswith(',') or first.endswith('.'):
	# 			first = first[:-1]
	# 		if first.startswith('-') or first.startswith(',') or first.startswith('.'):
	# 			first = first[1:]
	# 		if '...' in first:
	# 			first = first.replace('...', '')
	# 		lexemes[first] = vector
	#
	# with codecs.open('auto_output/lexemes_new.txt', 'w', 'utf-8') as f:
	# 	for k,v in lexemes.iteritems():
	# 		f.write(k + ' ' + v)


