seq1 = 'ATGTTATAG'

import re
p = re.compile('TT')
aa = p.finditer(seq1)
aba = [ab.start() for ab in aa]


print aba
