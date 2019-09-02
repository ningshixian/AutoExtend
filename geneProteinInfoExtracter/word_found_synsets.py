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

# embeddings=readEmbedFile('embedding\\wikipedia-pubmed-and-PMC-w2v.bin')
# with open('embedding\word.txt','w')as wirte:
#     for id in embeddings.keys():
#         wirte.write(id+'\n')
def change(word):
    '''
     输入word，word是string格式
     如果输入的word里面有空格，那么将空格变换为@@，输出变换后的word；没有空格的话，直接输出word
     e.g.输入‘hello world’输出‘hello@@world’
    '''
    if ' ' in word:
        kong_word = word.split(' ')
        tab_word = ''
        for ge_word in kong_word:
            tab_word += ge_word + '@@'
        word = tab_word.strip('@@')
    return word

def word_found_synset():
    embeddings=readEmbedFile('embedding\\wikipedia-pubmed-and-PMC-w2v.bin')
    write_id_word=dict()
    with codecs.open('gene_proteinData/synsets.txt',encoding='utf-8')as read_file:
        for line in tqdm(read_file.readlines()):
            id_words = line.strip('\n').split('\t')
            words = id_words[1].split('::,')
            id=id_words[0]
            for word in words:
                # vector = np.zeros(word_dim)
                word=change(word)
                word_split = word.split('@@')
                is_in_embeddings = 1
                for ele in word_split:
                    if ele.lower() not in embeddings:
                        is_in_embeddings = 0
                #     else:
                #         vector+=embeddings[ele.lower()]
                # if is_in_embeddings:
                #     vector=vector/len(word_split)
                if is_in_embeddings:
                    if id not in write_id_word:
                        write_id_word[id]=word+'::,'
                    # else:
                        # dict_word=write_id_word[id].split('::,')+word
                        # write_id_word[id]+=word+'::,'
    with codecs.open('extractedData/add/synsets.txt',encoding='utf-8')as read_file:
        for line in tqdm(read_file.readlines()):
            id_words = line.strip('::,\n').split('\t')
            words = id_words[1].split('::,')
            id = id_words[0]
            for word in words:
                # vector = np.zeros(word_dim)
                word_split = word.split('@@')
                is_in_embeddings = 1
                for ele in word_split:
                    if ele.lower() not in embeddings:
                        is_in_embeddings = 0
                #     else:
                #         vector+=embeddings[ele.lower()]
                # if is_in_embeddings:
                #     vector=vector/len(word_split)
                if is_in_embeddings:
                    if id not in write_id_word:
                        write_id_word[id] = word + '::,'
                    else:
                        dict_word=write_id_word[id].strip('::,').split('::,')
                        # print(dict_word)
                        dict_word.append(word)
                        # print(dict_word)
                        write_word=''
                        for ele in set(dict_word):
                            write_word+=ele+'::,'
                        write_id_word[id]=write_word

    with codecs.open('extractedData/synsets.txt','w',encoding='utf-8')as write:
        for key, value in write_id_word.items():
            # print(key,value)
            # print(key.encode('utf-8'), value.encode('utf-8'))
            write.write(key.encode('utf-8').decode('utf-8')+'\t'+value.encode('utf-8').decode('utf-8')+'\n')


def append_not_found():
    from tqdm import tqdm
    found_id_word=OrderedDict()
    with codecs.open('extractedData/synsets.txt',encoding='utf-8')as read_file:
        for line in tqdm(read_file.readlines()):
            id_words = line.strip('\n').split('\t')
            # words = id_words[1].split('::,')
            id=id_words[0]
            # write_word=''
            # for word in words:
                # word=change(word)
                # write_word+=word+'::,'
            found_id_word[id]=id_words[1]
    with codecs.open('extractedData/word_found/synsets.txt','w',encoding='utf-8')as write:
        with codecs.open('gene_proteinData/synsets.txt',encoding='utf-8')as read_file:
            lines = read_file.readlines()
        id_count=0
        for i in tqdm(range(len(lines))):
            line = lines[i]
            id_words = line.strip('\n').split('\t')
            id=id_words[0]
            if id not in found_id_word:
                # print(id)
                id_count+=1
                words = id_words[1].split('::,')
                write_word = ''
                for word in words:
                    word=change(word)
                    write_word+=word+'::,'
                # print(write_word)
                found_id_word[id]=write_word
        for key, value in found_id_word.items():
            write.write(key.encode('utf-8').decode('utf-8')+'\t'+value.encode('utf-8').decode('utf-8')+'\n')
    print(id_count)#85

def is_uni():
    with codecs.open('extractedData/word_found/synsets.txt',encoding='UTF-8')as read_2:
        id_count = 0
        uesd_id=dict()
        for line in tqdm(read_2.readlines()):
            id_word=line.strip('\n').split('\t')
            words=id_word[1]
            id=id_word[0].upper()
            if id not in uesd_id:
                uesd_id[id]=words
                id_count+=1
            else:
               print(line)
                # id_word
            #     print(id)
        print(id_count)

def is_id_found():
    found_id_word = OrderedDict()
    with codecs.open('gene_proteinData/synsets.txt', encoding='utf-8')as read_file:
        for line in tqdm(read_file.readlines()):
            id_words = line.strip('\n').split('\t')
            id = id_words[0]
            found_id_word[id] = id_words[1]
    with open('extractedData/synsets.txt',encoding='UTF-8')as read:
        for line in tqdm(read.readlines()):
            id_words = line.strip('\n').split('\t')
            id = id_words[0]
            if id not in found_id_word:
                print(line)


if __name__=='__main__':
    word_found_synset()
    append_not_found()
    # is_uni()
    # is_id_found()