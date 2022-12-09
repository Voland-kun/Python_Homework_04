#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import re

file1 = 'test_poly-1.txt'
file2 = 'test_poly-2.txt'

def get_poly_from_file(file):
    with open(str(file), 'r') as data:
        poly_str = data.read()
    return poly_str

def get_dct(stroka): #получаем словарь содержащий показатель степени : коэффициенты
    stroka = stroka.replace('x+', 'x^1+')
    stroka = stroka.replace('x-', 'x^1-')
    stroka = stroka.replace('=0', '')
    stroka = re.sub('[*|+]','', stroka)
    if stroka[-2] != '^':
        stroka = stroka + '^0'
    stroka = stroka.split('x')
    for i in range(1, len(stroka)):
        #if stroka[i].startswith('^') == True:
        if stroka[i][0] == '^':
            stroka[i-1] = stroka[i-1] + stroka[i][0:2]  #не работает для степеней больше 9
            stroka[i] = stroka[i][2:]
    stroka = [i.split('^') for i in stroka]
    poly_dict = {}
    for i in range(len(stroka)):
        poly_dict[int(stroka[i][1])] = int(stroka[i][0])
    print(poly_dict)
    return poly_dict

def poly_sum(poly1, poly2):
    result = ''
    max_ = 0
    dict1 = get_dct(poly1)
    dict2 = get_dct(poly2)
    key_lst_1 = list(dict1.keys())
    key_lst_2 = list(dict2.keys())
    max_1 = max(key_lst_1)
    max_2 = max(key_lst_2)
    if max_1 >= max_2:
        max_ = max_1
    else: max_ = max_2
    for i in range(max_, -1, -1):
        if dict1.get(i, 0) + dict2.get(i, 0) == 0:
            pass
        elif dict1.get(i, 0) + dict2.get(i, 0) < 0:
            result = result + f'{dict1.get(i, 0) + dict2.get(i, 0)}*x^{i}'
        else:
            result = result + f'+{dict1.get(i, 0) + dict2.get(i, 0)}*x^{i}'
    result = result + '=0'
    result = result.replace('-1*x^', '-x^')
    result = result.replace('+1*x^', '+x^')
    result = result.replace('*x^0', '')
    result = result.replace('x^1', 'x')
    print(result)
    return result

pol1 = get_poly_from_file(file1)
pol2 = get_poly_from_file(file2)


print(pol1)
print(pol2)
with open(f'polynom_sum.txt', 'w') as file:
    file.write(poly_sum(pol1, pol2))