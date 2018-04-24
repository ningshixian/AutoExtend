function [A, dictA, dictPOS] = loadTxtFile( filename )

	fprintf('Reading word vectors ... \n');
    
    fileID = fopen(filename);   % fid（文件识别符）= -1: 一般来说可能会是因为没有权限或者文件路径错误之类的问题
    fprintf('fileID %f\n', fileID);
    line = fgetl(fileID);       % fgetl从已经打开的文件中读取一行，并且丢掉末尾的换行符。
    dim = length(strfind(line,' '));
    fprintf('dim %f\n', dim);
    
    frewind(fileID);      %位置指针移至文件首部
    
    textformat = ['%s', repmat(' %f',1,dim)];
    Table = textscan(fileID,textformat);       % 输出C为1*column的细胞数组，每个数组中存放每列的数据
 
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