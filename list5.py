li = [3,1,1,2,0,0,2,3,3]

dic = {}

for aa in li:
    if dic.has_key(aa) == False:
        dic[aa] = 1
    else:
        dic[aa] += 1

print dic
