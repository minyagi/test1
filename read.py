rr = open('test.txt', 'r')

xr = rr.xreadlines()
rr.close()
for ii in xr:
    print(ii)
'''
with open('test.txt', 'r') as fr:
    for line in fr:
        print(line) #추천합니다.리스트를 만들지 않음.
'''
