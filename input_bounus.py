import sys

print(sys.argv)
#실행을 할 때 리스트에 파라미터들이 이용됨.
#파라미터를 볼 수 있음?

name = sys.argv[1]
'''
print('Hello ' + name)
'''

print('bwa '+name+'1.fastq.gz '+name+'_2.fastq.gz')
print('picard MarkDuplicate '+name+'.bam')


