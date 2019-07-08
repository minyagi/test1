seq1 = 'ATGTTATAG'
tr = {'A':'T','T':'A','C':'G','G':'C'}
'''
tr = {'ATCG':'TAGC'}
print seq1.translate(tr)
'''

li_s = [tr[ss] for ss in seq1]

li_s = ''.join(li_s)

print li_s
