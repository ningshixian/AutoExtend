gene_proteinData: The file is too large to upload
Gene_info_processed: The file is too large to upload
Uniprot_sprot.dat: The file is too large to upload

Used_synsets.txt: Synsets used in the experiment
Synsets.txt: Replace all the ids in used_synsets.txt with uppercase and deduplicate. The synset of the same id is deduplicated and put together. Convert the Greek letters to English phonetic


extractedData:
Origin:
Synsets.txt: Find the protein and gene name in the corresponding gene in the corresponding gene according to the id in gene_proteinData/synsets.txt, and output each line: id+'\t'+'name_1::,name_2::,' +'\n'

Add:
Synsets.txt: Find the protein and gene name in the corresponding gene in the corresponding gene according to the id in gene_proteinData/synsets.txt, and find the corresponding line in the output gene_proteinData/synsets.txt of the id, and output each line. :id+'\t'+'name_1::,name_2::,'+'\n'

Word_found:
Synsets.txt: In the gene_proteinData/synsets.txt and extractedData/add/synsets.txt, find the words that can be found in the word vector file according to the space segmentation, and output according to the id. The ids that are not found in all are output according to the corresponding line of gene_proteinData/synsets.txt.
Lexemes.txt: morpheme
Words.txt: After splitting in synsets.txt, you can find the average output word and vector of the word vector. Randomly initialized np.random.uniform(-0.1,0.1,200)

The order of running programs: synsets.py -> word_found_synsets.py -> lexemes.py -> word.py -> AutoExtend.m
