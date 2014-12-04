clear all;
[a b] = system(['ls messages > flist.txt']);
count = 1;
flist = fopen('flist.txt');
fname = fgetl(flist);
while ischar(fname)
    s = struct();
    f = fopen(['messages/',fname]);
    
    line = fgetl(f);
    while strcmp(line,'Protein sequence information:')==0
        line = fgetl(f);
    end
    line = fgetl(f);
    line2 = fgetl(f);
    while line2(1) ~= '.'
        line = [line,line2(2:end)];
        line2 = fgetl(f);
    end        
    s.seq = line;
    line = fgetl(f);
    res = textscan(f,'%d %c %f %f %f');
    s.hseup = res{3};
    s.hsedown = res{4};
    s.cn = res{5};
    assert(length(s.hseup) == length(s.seq))
    fclose(f);
    data(count) = s;
    count = count + 1;
    fname = fgetl(flist);

end
fclose(flist);
save hsepred.mat data
