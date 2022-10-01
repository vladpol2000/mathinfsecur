def route_encryption(orig_string, pswd, n):
    string = orig_string.replace(' ','')    #Убираем все пробелы из строки
    m = len(string)//n+bool(len(string)%n)  #Находим количество блоков заданной длины n
    string += 'а'*(m*n-len(string))         #Добавляем в конец строки символ а умноженный на выражение в скобках для соответствия размеров матрицы m*n
    nums = [sorted(pswd).index(c) for c in pswd]    #Создаем список индексов букв пароля в соответствие с сортировкой по алфавиту
    print(nums)
    result = ''
    for i in range(n):
        for j in range(m):
            result += string[j*n + nums.index(i)].upper()   #Проходимся при помощи двойного цикла по строке, составляя зашифрованную строку в соответствие с паролем 
    return result


def lattice_encryption(orig_string, pswd, k, xys):
    string = orig_string.replace(' ','')
    matr = []
    for i in range(k*2):
        matr.append(['.']*(k*2))    #Заполняем нашу матрицу размерностью 2k точками
    u = 0
    for i in range(4):  #Данный цикл создан для наложения решетки после переворота на 90 градусов. На 4 шаге наша матрица уже должна быть заполнена
        for x, y in xys:
            matr[x][y] = string[u]  #Заполняем "прорези" решётки элементами нашей строки
            u+=1
        xys = [(y, 2*k-1-x) for x, y in xys]    #Поворачиваем решётку на 90 градусов
    res = ''
    for i in range(k*2):
        for c in matr[i]:
            res += c
    return route_encryption(res, pswd, 2*k) #Шифруем получившуюся строку при промощи пароля и функции для маршрутного шифрования


def vigenere_encryption(orig_string, pswd):
    string = orig_string.replace(' ','')
    pswd = (pswd*(len(string)//len(pswd)+1))[:len(string)]  #Продлеваем наш пароль до конца введенной строки
    alphabet = [chr(c) for c in range(ord('а'), ord('я') + 1)]  #Реализация алфавита из прошлой лабораторной работы
    matr = []
    res = ''
    for i in range(32):
        matr.append(alphabet)
        alphabet = alphabet[1:] + [alphabet[0]]     #Записываем матрицу со смещением от i до конца и в конец добавляем от 0 до i
        #print(matr[i])
    for p,s in zip(pswd,string):
        res += matr[ord(s)-ord('а')][ord(p)-ord('а')]
    return res.upper()  #Пробегаемся сразу по двум спискам и вычитаем по вертикали и горизонтали первый элемент для нахождения номера строки и столбца заменяющий буквы   

#print(route_encryption('нельзя недооценивать противника', 'пароль', 6))

#print(lattice_encryption('договор подписали', 'шифр', 2, [(0,3), (3,2), (2,3), (2,1)]))

print(vigenere_encryption('криптография серьезная наука', 'математика'))