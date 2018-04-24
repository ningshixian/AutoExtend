function [A, dictA, dictPOS] = loadTxtFile( filename )

	fprintf('Reading word vectors ... \n');
    
    fileID = fopen(filename);   % fid���ļ�ʶ�����= -1: һ����˵���ܻ�����Ϊû��Ȩ�޻����ļ�·������֮�������
    fprintf('fileID %f\n', fileID);
    line = fgetl(fileID);       % fgetl���Ѿ��򿪵��ļ��ж�ȡһ�У����Ҷ���ĩβ�Ļ��з���
    dim = length(strfind(line,' '));
    fprintf('dim %f\n', dim);
    
    frewind(fileID);      %λ��ָ�������ļ��ײ�
    
    textformat = ['%s', repmat(' %f',1,dim)];
    Table = textscan(fileID,textformat);       % ���CΪ1*column��ϸ�����飬ÿ�������д��ÿ�е�����
 
    dictA = Table{1,1}(:, 1);       
    fprintf('word.txt length(dictA) %f\n', length(dictA));       % 636950
    A = zeros(length(dictA),dim);
    for d=1:dim
        A(:,d) = table2array(Table(:, d+1));
    end
    
    fclose(fileID);
    
    if nargout > 2
        
        [dictA, dictPOS] = strtok(dictA_, '%');
        dictPOS = strrep(dictPOS, '%', '');
    
    else
        
        dictA = strrep(dictA, '%n', '');
        dictA = strrep(dictA, '%v', '');
        dictA = strrep(dictA, '%a', '');
        dictA = strrep(dictA, '%r', '');
        dictA = strrep(dictA, '%u', '');
        
    end

	fprintf('done!\n');

end