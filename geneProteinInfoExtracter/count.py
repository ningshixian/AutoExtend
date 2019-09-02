import numpy as np
import word2vec
from collections import OrderedDict
from tqdm import tqdm
word_dim=200
def readEmbedFile(embFile):
    """
    读取预训练的词向量文件，引入外部知识
    """
    print("\nProcessing Embedding File...")
    embeddings = OrderedDict()
    embeddings["PADDING_TOKEN"] = np.zeros(word_dim)
    embeddings["UNKNOWN_TOKEN"] = np.random.uniform(-0.1, 0.1, word_dim)
    embeddings["NUMBER"] = np.random.uniform(-0.25, 0.25, word_dim)

    # 针对二进制格式保存的词向量文件
    model = word2vec.load(embFile)
    print('加载词向量文件完成')
    for i in tqdm(range(len(model.vectors))):
        vector = model.vectors[i]
        word = model.vocab[i].lower()   # convert all characters to lowercase
        embeddings[word] = vector


    # with open(embFile,'r', encoding='UTF-8') as f:
    #     lines = f.readlines()
    # for i in range(len(lines)):
    #     line = lines[i]
    #     if len(line.split())<=2:
    #         continue
    #     values = line.strip().split()
    #     word = values[0].lower()
    #     vector = np.asarray(values[1:], dtype=np.float32)
    #     embeddings[word.lower()] = vector
    return embeddings

embeddings=readEmbedFile('embedding\\wikipedia-pubmed-and-PMC-w2v.bin')

uni_word_count=0
find_uni_word_count=0
total_word_count=0
find_total_word_count=0
uni_word=dict()
write_id_word=dict()
with open('gene_proteinData/synsets.txt',encoding='utf-8')as read_file:
    for line in tqdm(read_file.readlines()):
        id_words=line.strip('\n').split('\t')
        words=id_words[1].split('::,')
        for word in words:
            if word not in uni_word:
                uni_word_count+=1
                word_split=word.split(' ')
                is_in_embeddings=0
                for ele in word_split:
                    if ele.lower()  in embeddings:
                        is_in_embeddings=1
                if is_in_embeddings:
                    find_uni_word_count+=1
                    find_total_word_count += 1
                uni_word[word]=is_in_embeddings
                total_word_count += 1
            else:
                if uni_word[word]:
                    find_total_word_count+=1
                total_word_count+=1
print('uni_word_count',uni_word_count,
'find_uni_word_count',find_uni_word_count,
'total_word_count',total_word_count,
'find_total_word_count',find_total_word_count,
)
#uni_word_count 6022 find_uni_word_count 5364 total_word_count 28664 find_total_word_count 26354    只要有一个在里面就算有
#uni_word_count 6022 find_uni_word_count 5326 total_word_count 28664 find_total_word_count 26275    全都找到才算找到