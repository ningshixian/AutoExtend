function [] = writeVectors(varargin)
    
%     folder = varargin{1};
%     experiment = varargin{2};
%     folder = 'C:\Users\Administrator\Desktop\AutoExtend-master\WordNetExtract\output_a\';
%     folder =  'F:\B910\AutoExtend-master\geneExtract\extracted-mul\';
    folder = 'E:\proteinInfoExtracter\extractedData\data2\'
    experiment = 'naive\';
    
    writeWords = true;
    writeSynsets = true;
    writeLexemes = true;    
    
    if (nargin == 5)   
        writeWords = varargin{3};
        writeSynsets = varargin{4};
        writeLexemes = varargin{5};
    end
    
    file = strcat(folder, experiment, '/outputVectors.txt');

    [W , dictW] = loadTxtFile(strcat(folder, 'words.txt'));
    [dictS, dictSID] = loadSynsetFile(folder);
    
    fileID = fopen(strcat(folder, experiment, '/theta.txt'));  
    line = fgetl(fileID);       % fgetl从已经打开的文件中读取一行，并且丢掉末尾的换行符。
    dim = length(strfind(line,' '));
    fprintf('dim %f\n', dim);
    
    frewind(fileID);      %位置指针移至文件首部
    
    textformat = ['%d', ' %d', repmat(' %f',1,dim-1)];
    Table = textscan(fileID,textformat);       % 输出C为1*column的细胞数组，每个数组中存放每列的数据
    
    dictA = Table{1,1}(:, 1); 
    fName = strcat(folder, experiment, '/t.txt');
    dlmwrite(fName,dictA,'delimiter','\n','newline','pc','precision',6);
    fprintf('写入 t.txt完成')

    fprintf('theta length(dictA) %f\n', length(dictA));       % 1179876
    Theta = zeros(length(dictA),dim+1);
    for d=1:dim+1
        Theta(:,d) = table2array(Table(:, d));
    end
    
    fclose(fileID);
    
%     Theta = importdata(strcat(folder, experiment, '/theta.txt'), ' ');
    fprintf('Calculating synset vectors ... ');
    S = zeros(size(dictS, 1), size(W,2));
    for l=1:size(Theta, 1)
        w = Theta(l,1);
        s = Theta(l,2);
        theta = Theta(l, 3:end);
        S(s,:) = S(s,:) + (W(w,:) .* theta);
    end
    fprintf('done!\n');
        
    outputSize = 0;
    if (writeWords == true)
        outputSize = outputSize + size(dictW, 1);
    end
    if (writeLexemes == true)
        outputSize = outputSize + size(Theta, 1);
    end
    if (writeSynsets == true)
        outputSize = outputSize + size(dictS, 1);
    end
    
    fid = fopen(file, 'w');
    fprintf(fid, '%d %d\n',outputSize, size(W,2));
    fclose(fid);

    if (writeWords == true)
        fprintf('Writing word vectors ... ');
        writeToFile(file, 'a', W, dictW);
        fprintf('done!\n');
    end
    
    if (writeSynsets == true)
        
        fprintf('Writing synset vectors ... ');
        writeToFile(file, 'a', S, dictS);
        fprintf('done!\n');
    end
    
    if (writeLexemes == true)
        
        fileID2 = fopen(strcat(folder, experiment, '/iota.txt'));  
        line2 = fgetl(fileID2);       % fgetl从已经打开的文件中读取一行，并且丢掉末尾的换行符。
        dim2 = length(strfind(line2,' '));
        fprintf('dim %f\n', dim2);

        frewind(fileID2);      %位置指针移至文件首部

        textformat2 = ['%d', ' %d', repmat(' %f',1,dim2-1)];
        Table2 = textscan(fileID2,textformat2);       % 输出C为1*column的细胞数组，每个数组中存放每列的数据

        dictA2 = Table2{1,1}(:, 1);       
        fprintf('iota length(dictA) %f\n', length(dictA2));       % 1179877
        Iota = zeros(length(dictA2),dim2+1);
        for d=1:dim2+1
            Iota(:,d) = table2array(Table(:, d));
        end

        fclose(fileID);
        
%         Iota = importdata(strcat(folder, experiment, '/iota.txt'), ' ');
        Theta = sortrows(Theta, [1 2]);
        Iota = sortrows(Iota, [1 2]);
        
        if (sum(sum(Theta(:,1:2)-Iota(:,1:2))) ~= 0)
            fprintf('Iota and Theta file do not match. Lexemes vector might be screwed.\n');
        end
        
        fprintf('Calculating lexeme vectors ... ');
        L = zeros(size(Theta, 1), size(W,2));
        dictL = cell(size(Theta, 1), 1);
        for l=1:size(Theta, 1)
            w = Theta(l,1);
            s = Theta(l,2);
            theta = Theta(l, 3:end);
            iota = Iota(l, 3:end);
            L(l,:) = ((W(w,:) .* theta) + (S(s,:) .* iota)) / 2;
            dictL{l} = strcat(dictW{w}, '-', dictSID{s});
        end
        fprintf('done!\n');
    
        fprintf('Writing lexeme vectors ... ');
        writeToFile(file, 'a', L, dictL);
        fprintf('done!\n');
    end

end

function [] = writeToFile(file, mode, A, dictA)

    fid = fopen(file, mode);

    for i=1:size(dictA,1)
        fprintf(fid, '%s', dictA{i});
        fprintf(fid,' %f',A(i,:));
        fprintf(fid,'\n');
    end

    fclose(fid);

end
