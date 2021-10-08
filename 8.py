try:
    numb = int(input('Введите число:'))
    sist = int(input('Введите целевую систему счисления: '))
    while sist != 2 and sist != 8:
         print('Выберете либо 2-ичную систему счисления, либо 8-ичную')
         sist = int(input())
    if sist == 2:
        print(bin(numb)[2:])
    if sist == 8:
        print(oct(numb)[2:])
except ValueError: 
    print('Это не число. Введите число.')         