try:
    num = int(input('Enter: '))
    print(10 / num)
except NameError:
    print('plz enter number')
except ZeroDivisionError:
    print('plz enter number over 0')

