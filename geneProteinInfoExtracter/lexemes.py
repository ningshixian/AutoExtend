from tqdm import tqdm
def get_lexems():
    '''
    根据synsets提取词素
    输出：lexemes.txt文件
         第一列：同义词集单词的编号（按照出现的先后依次编号，如果同一个单词出现多次，采取第一次出现的编号）
         第二列：同义词集的行号
    '''
    line_count=1
    word_count=1
    exited_entity = {}
    with open ('extractedData/word_found/lexemes.txt','w',encoding='utf-8')as write_file:
        with open('extractedData/word_found/synsets.txt',encoding='utf-8') as read_file:
            for line in tqdm(read_file.readlines()):
                ele=line.strip('::,\n').split('\t')
                print(ele)
                words=ele[1].split('::,')
                for word in words:
                    if word not in exited_entity:
                        write_file.write(str(word_count)+' '+str(line_count)+'\n')
                        exited_entity[word] = word_count
                        word_count += 1
                    else:
                        used_word_count = exited_entity[word]
                        write_file.write(str(used_word_count) + ' ' + str(line_count) + '\n')
                line_count+=1
    print(word_count-1)# lexemes：28481
    print(line_count-1)# lexemes：9803

if __name__=='__main__':
    get_lexems()


