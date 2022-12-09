#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100) многочлена и записать в файл многочлен степени k(до 6 степени).*

from random import randint

def input_int():
    while True:
        try:
            user_number = input('Введите целое число: ')
            user_number = int(user_number)
            return user_number
        except ValueError:
            print('Введено не целое число.')

def polynomial(k):
    poly_str = ''
    a_lst = [randint(-100, 100) for i in range(k + 1)]
    print(a_lst)
    mono_lst = [f'{a_lst[i]}*x^{k - i}' for i in range(k+1) if a_lst[i] != 0]
            
    #print(mono_lst)

    if len(mono_lst) != 0:
        poly_str = poly_str + mono_lst[0]
        for i in range(1, len(mono_lst)):
            mono_lst[i] = mono_lst[i].replace('x^1', 'x').replace('*x^0', '')
            if (mono_lst[i])[0] != '-':
                poly_str = poly_str + f'+{mono_lst[i]}'
            else:
                poly_str = poly_str + mono_lst[i]
        #print(mono_lst)
        poly_str = poly_str + '=0'
    else:
        print('Не повезло.')
    
    print(poly_str)
    return poly_str

for i in range(1, 3):
    k = input_int()
    with open(f'polynom-{i}.txt', 'w') as file:
        file.write(polynomial(k))
        print()