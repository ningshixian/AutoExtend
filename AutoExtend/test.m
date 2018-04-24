% folder = 'G:\ningshixian\CilinExtract\data\';
% % folder = 'E:\workspace\WordNetExtract\output\';
% 
% [W , ~] = loadTxtFile(strcat(folder, 'words.txt'));
% dim = size(W,2); % m = size(X,dim);%���ؾ����������������dim=1����������dim=2��������
% num_iters = 1000; %num_iters = 0;
% fprintf('dim %f\n', dim);


folder =  'G:\python-workspces\ningshixian\CilinExtract\data\';
RelationFiles = cell(2,1); % 2x1��cell����
RelationFiles{1} = 'similar.txt';
RelationFiles{2} = 'constrain.txt';

RelationMap = [];
for i=1:size(RelationFiles, 1)
	Table = readtable(strcat(folder, RelationFiles{i}), 'ReadVariableNames', false, 'Delimiter', ' ');
	if isempty(Table)
        continue;
    end
    RelationMap = [RelationMap ; table2array(Table(:, 1:2))];
end

for i=1:size(RelationMap, 1)
    fprintf('%s\n', RelationMap);
end