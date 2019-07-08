num1 = 21

if num1 % 3 == 0 and num1 % 7 == 0:
    print(num1, '은 3의 배수이며 7의 배수')
elif num1 % 3 == 0:
    print(num1, '은 3의 배수')
elif num1 % 7 == 0:
    print(num1, '은 7의 배수')
else:
    print('--')
