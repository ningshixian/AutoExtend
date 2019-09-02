# _*_ coding:utf-8 _*_
from tqdm import tqdm
import codecs
def add_synset():
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
    # with open('extractedData/words.txt')as read_file_word:
    #     for line in tqdm(read_file_word.readlines()):
    #         ele=line.strip('\n').split(' ')
    #         word[ele[0]]=index
    #         index+=1

    with codecs.open ('gene_proteinData/synsets.txt',encoding='utf-8')as read_synset_file:
        '''
        记录实验使用的synsets的id
        '''
        id_count=0
        uesd_id=dict()
        for line in tqdm(read_synset_file.readlines()):
            id_word=line.strip('\n').split('\t')
            uesd_id[id_word[0].upper()]=id_count
            id_count+=1



    with codecs.open('extractedData/origin/synsets.txt','w',encoding='utf-8')as write_file:
        '''
        将基因名字和蛋白质名字都输出
        '''
        with codecs.open('gene_proteinData/gene_info_processed',encoding='utf-8')as read_file:
            for line in tqdm(read_file.readlines()):
                id_word=line.strip('\n').split('\t')
                if id_word[0] in uesd_id:
                    write_file.write(id_word[0]+'\t'+id_word[1]+'\n')
        with codecs.open('gene_proteinData/uniprot_sprot.dat',encoding='utf-8')as read_file:
            is_have_id=0
            syn_name = ''
            real_id=''
            is_write=0
            for line in tqdm(tqdm(read_file.readlines())):
                if line[:2]=="AC":
                    ids = line.strip(';\n').split('   ')
                    # print(ids)
                    id = ids[1].split(';')
                    real_id=id[0]
                    if real_id in uesd_id:
                        print_id=real_id
                        is_have_id=1
                        is_write=1
                if line[:2] == "DE":
                    if 'Flags:'in line:
                        is_have_id=0
                    if 'Includes:'in line:
                        is_have_id = 0
                    if 'Contains:'in line:
                        is_have_id = 0
                    if is_have_id:
                        names=line.strip(';\n').split('=')
                        name_anno=names[1].split(' {')
                        name=change(name_anno[0])
                        syn_name+=name+'::,'
                if line[:2] == 'GN':
                    if is_have_id:
                        id_names=line.strip(';\n').split('   ')
                        names=id_names[1].split('; ')
                        for ele in names:
                            if '='in ele:
                            # print(ele)
                                name_name=ele.split('=')
                                if ', 'in name_name[1]:
                                    name_multi=name_name[1].split(', ')
                                    for name in name_multi:
                                        if ' {'in name:
                                            w_name=name.split(' {')
                                            syn_name+=change(w_name[0])+'::,'
                                        else:
                                            if 'ECO:' not in name:
                                                syn_name += change(name) + '::,'
                                else:
                                    if ' {' in name_name[1]:
                                        w_name = name_name[1].split(' {')
                                        syn_name += change(w_name[0]) + '::,'
                                    else:
                                        if 'ECO:' not in name:
                                            syn_name += change(name_name[1]) + '::,'
                            else:
                                if ', 'in ele:
                                    name_multi=ele.split(', ')
                                    for name in name_multi:
                                        if ' {'in name:
                                            w_name=name.split(' {')
                                            syn_name+=change(w_name[0])+'::,'
                                        else:
                                            if 'ECO:'not in name:
                                                syn_name += change(name) + '::,'
                                else:
                                    if ' {' in ele:
                                        w_name = ele.split(' {')
                                        syn_name += change(w_name[0]) + '::,'
                                    else:
                                        if 'ECO:' not in name:
                                            syn_name += change(ele) + '::,'
                if line=='//\n'and is_write:
                    write_file.write(print_id+'\t'+syn_name+'\n')
                    is_have_id=0
                    syn_name=''
                    is_write=0

    with codecs.open('extractedData/origin/synsets.txt')as read_2:
        id_count = 0
        uesd_id=dict()
        for line in tqdm(read_2.readlines()):
                id_word=line.strip('\n').split('\t')
                uesd_id[id_word[0]]=id_word[1]
                id_count+=1
    with codecs.open('gene_proteinData/synsets.txt',encoding='UTF-8')as read_1:
        count=0
        for line in tqdm(read_1.readlines()):
            id_word = line.strip('\n').split('\t')
            if id_word[0].upper()not in uesd_id:
                word=''
                for ele in id_word[1].split('::,'):
                    ele=change(ele)
                    word+=ele+'::,'
                uesd_id[id_word[0].upper()]=word
                count+=1
        print(count)
    with codecs.open('extractedData/add/synsets.txt','w',encoding='UTF-8')as write:
        for key, value in uesd_id.items():
            print(key, value)
            write.write(key+'\t'+value+'\n')

def greek2english(sent):
    greek=dict(α='alpha',β='beta',γ='gamma',δ='deta',ε='epsilon',ζ='zeta',η='eta',θ='theta',ι='iota',κ='kappa',λ='lambda',
               μ='mu',ν='nu',ξ='xi',ο='omicron',π='pi',ρ='rho',σ='sigma',τ='tau',υ='upsilon',φ='phi',χ='chi',ψ='psi',ω='omega',
                Α='alpha',Β='beta',Γ='gamma',Δ='deta',Ε='epsilon',Ζ='zeta',Η='eta',Θ='theta',Ι='iota',Κ='kappa',Λ='lambda',
               Μ='mu',Ν='nu',Ξ='xi',Ο='omicron',Π='pi',Ρ='rho',Σ='sigma',Τ='tau',Υ='upsilon',Φ='phi',Χ='chi',Ψ='psi',Ω='omega')
    greek['‐']='-'
    greek['−'] = '-'
    for ele in greek.keys():
        if ele in sent:
            position=sent.find(ele)
            while position!=-1:
                sent=sent[:position]+greek[ele]+sent[position+1:]
                position = sent.find(ele)
    return sent
# print(greek2english('α-GPDH'))
def merge_id():
    '''
    把id相同的拼接在一起，且将希腊字母转换为英文注音
    :return:
    '''
    with codecs.open('gene_proteinData/used_synsets.txt',encoding='UTF-8')as read_2:
        id_count = 0
        uesd_id=dict()
        for line in tqdm(read_2.readlines()):
            id_word=line.strip('\n').split('\t')
            words=id_word[1]
            words=greek2english(words)
            id=id_word[0].upper()
            if id not in uesd_id:
                uesd_id[id]=words
                id_count+=1
            else:
                word=uesd_id[id].split('::,')+words.split('::,')
                # print(word)
                word=set(word)
                write_word=''
                for ele in word:
                    write_word+=ele+'::,'
                write_word=write_word.strip('::,')
                uesd_id[id]=write_word
                # id_word
            #     print(id)
        print(id_count)

    with codecs.open('gene_proteinData/synsets.txt','w',encoding='UTF-8')as write:
        for key,value in uesd_id.items():
            write.write(key+'\t'+value+'\n')

if __name__=='__main__':
    merge_id()
    add_synset()
