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

    for i in range(k+1):
        if a_lst[i] == 0:
            pass
        elif len(poly_str) == 0 and k-i == 0 \
                or a_lst[i] < 0 and k-i == 0:
            poly_str = poly_str + f'{a_lst[i]}'
        elif len(poly_str) == 0 and k-i == 1 \
                or a_lst[i] < 0 and k-i == 1:
            poly_str = poly_str + f'{a_lst[i]}*X'
        elif len(poly_str) == 0 and k-i not in [0, 1] \
                or a_lst[i] < 0 and k-i > 1:
            poly_str = poly_str + f'{a_lst[i]}*X^{k-i}'
        elif a_lst[i] > 0 and len(poly_str) != 0:
            if k-i == 0:
                poly_str = poly_str + f'+{a_lst[i]}'
            elif k-i == 1:
                poly_str = poly_str + f'+{a_lst[i]}*X'
            else:
                poly_str = poly_str + f'+{a_lst[i]}*X^{k-i}'
    poly_str = poly_str + '=0'
    print(poly_str)            
    return poly_str

for i in range(1, 3):
    k = input_int()
    with open(f'polynom-{i}.txt', 'w') as file:
        file.write(polynomial(k))
        print()