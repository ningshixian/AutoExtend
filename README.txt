gene_proteinData��
	gene_info_processed�����������
	uniprot_sprot.dat�������ʵ�����
	used_synsets.txt��ʵ���õ���synsets
	synsets.txt����used_synsets.txt�е�idȫ�����ɴ�д��ȥ�أ�����ͬ��id��synsetȥ�غ����һ�𡣽����е�ϣ����ĸת��ΪӢ��ע��


extractedData��
	origin:
		synsets.txt������gene_proteinData/synsets.txt�����id�ڶ�Ӧ�Ļ������һ������͵����������ҵ��׺ͻ����������ÿ�У�id+'\t'+'name_1::,name_2::,'+'\n'

	add��
		synsets.txt������gene_proteinData/synsets.txt�����id�ڶ�Ӧ�Ļ������һ������͵����������ҵ��׺ͻ��������Ҳ���id�����gene_proteinData/synsets.txt�����Ӧ�����У����ÿ�У�id+'\t'+'name_1::,name_2::,'+'\n'

	word_found��
		synsets.txt����gene_proteinData/synsets.txt��extractedData/add/synsets.txt�����Ұ��տո��зֺ��ܹ��ڴ������ļ���ȫ���ҵĵ��Ĵʣ�����id���������ȫ���Ҳ�����id������gene_proteinData/synsets.txt�Ķ�Ӧ�������
		lexemes.txt������
		words.txt����synsets.txt�е��зֺ�ȫ�����ҵ�����������ƽ������ʺ��������Ҳ����������ʼ��np.random.uniform(-0.1,0.1,200��

�ܳ����˳��synsets.py -> word_found_synsets.py -> lexemes.py -> word.py -> AutoExtend.m