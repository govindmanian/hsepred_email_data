load hsepred

f = fopen('sequence_list.txt');

seq = [];
i = 1;
line = fgetl(f);
while ischar(line)
    seq{i} = line;
    i = i  +1;
    line = fgetl(f);
end

fclose(f);

for i = 1:length(data)
    seq2{i} = data(i).seq;
end

w = fopen('seq_leftover2.txt','w');
for i = 1:length(seq)
    if isempty(find(strcmpi(seq{i},seq2)))
        fprintf(w,'%s\n',seq{i});
    end
end
fclose(w);
