
i = input('enter: ')

try:
    i = int(i)
    print(i,'is number')

except:
    print(i, 'is character')

'''
if i.isalpha():
    print('%i는 문자.' % i)
else i.isalpha():
    print('%s는 숫자.' %i)
'''

