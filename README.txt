gene_proteinData：
	gene_info_processed：基因的数据
	uniprot_sprot.dat：蛋白质的数据
	used_synsets.txt：实验用到的synsets
	synsets.txt：将used_synsets.txt中的id全部换成大写，去重，其中同个id的synset去重后放在一起。将其中的希腊字母转换为英文注音


extractedData：
	origin:
		synsets.txt：根据gene_proteinData/synsets.txt里面的id在对应的基因中找基因名和蛋白数据中找蛋白和基因名，输出每行：id+'\t'+'name_1::,name_2::,'+'\n'

	add：
		synsets.txt：根据gene_proteinData/synsets.txt里面的id在对应的基因中找基因名和蛋白数据中找蛋白和基因名，找不到id的输出gene_proteinData/synsets.txt里面对应的那行，输出每行：id+'\t'+'name_1::,name_2::,'+'\n'

	word_found：
		synsets.txt：在gene_proteinData/synsets.txt和extractedData/add/synsets.txt里面找按照空格切分后能够在词向量文件中全都找的到的词，按照id输出。其中全都找不到的id，按照gene_proteinData/synsets.txt的对应行输出。
		lexemes.txt：词素
		words.txt：将synsets.txt中的切分后全都能找到词向量的求平均输出词和向量，找不到的随机初始化np.random.uniform(-0.1,0.1,200）

跑程序的顺序：synsets.py -> word_found_synsets.py -> lexemes.py -> word.py -> AutoExtend.m