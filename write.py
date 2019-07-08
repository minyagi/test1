f = open('write_sample.txt', 'w')

f.write('Hello\n')
f.write('write_sample test file\n')

f.close()

fr = open('test.txt', 'r')
ff = open('write_sample1.txt', 'w')
fx = fr.xreadlines()
for ii in fx:
    ff.write(ii)

fr.close()
ff.close()

'''
with open('test1.txt', 'w') as fw:
    with open('test.txt', 'r') as fr:
        for line in fr:
            #fw.write(line)
            chr = line.split('\t')[0]
            chi = line.split('\t')[1]
            ref = line.split('\t')[3]
            mut = line.split('\t')[4]


