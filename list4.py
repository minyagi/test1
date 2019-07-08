li = [3,1,1,2,0,0,2,3,3]
ma = 0
mi = 1000

for aa in li:
    if mi > aa:
        mi = aa
    elif mi < aa:
        continue

for aa in li:
    if ma < aa:
        ma = aa
    elif ma > aa:
        continue
print mi, ma
