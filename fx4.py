
def ssum():
    i = input('enter the number: ')
    i = int(i)
    b = 0
    while i > 0:
        b = b + i
        i -= 1
    return b

b = ssum()
print(b)
