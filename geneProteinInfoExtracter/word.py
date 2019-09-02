# _*_ coding:utf-8 _*_
import numpy as np
import word2vec
import codecs
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
def print_word():
    embeddings=readEmbedFile('embedding\\wikipedia-pubmed-and-PMC-w2v.bin')
    # embeddings={}

    index=0
    uni_word=dict()
    count_num=0

    with codecs.open ('extractedData/word_found/words.txt','w',encoding='utf-8')as write_file:
        with codecs.open('extractedData/word_found/synsets.txt',encoding='utf-8') as read_file:
            for line in tqdm(read_file.readlines()):
                ele=line.strip('\n').split('\t')
                words=ele[1].split('::,')[:-1]
                for word in words:
                    if word not in uni_word:
                        uni_word[word] = index
                        index += 1
                        vec = ''
                        if '@@'not in word:
                            if word.lower() in embeddings:
                                arr = embeddings[word.lower()]
                            else:
                                arr=np.random.uniform(-0.1,0.1,size=word_dim)
                            for dim in arr:
                                vec += str(dim) + ' '
                            vec = vec.strip() + '\n'
                            write_file.write(str(word)+' '+vec)
                            count_num += 1
                        else:
                            split_word=word.split('@@')
                            arr=np.zeros(word_dim)
                            arr_count = 0
                            is_embedding=1
                            for ele in split_word:
                                if ele.lower() in embeddings:
                                    arr += embeddings[ele.lower()]
                                    arr_count += 1
                                else:
                                    is_embedding=0
                            if is_embedding:
                                arr = arr / arr_count
                            else:
                                arr=np.random.uniform(-0.1,0.1,size=word_dim)
                            for dim in arr:
                                vec += str(dim) + ' '
                            vec = vec.strip() + '\n'
                            write_file.write(str(word) + ' ' + vec)
                            count_num += 1

    print('登录词数量: %d' % count_num)#27580
    print('总共: %d' % index)#27580

if __name__ == '__main__':
    print_word()