from random import randint
import math

def test_ferm(n):
    flag = True
    for i in range(10):
        a = randint(2, n - 2)
        r = (a**(n-1)) % n
        if r != 1:
            flag = False   
    if flag == True:
        return('Число n, вероятно, простое')
    else:
        return('Число n  составное') 


def jacobi_symbol(a, b):
    even = lambda x: x%2==0  # lambda функция для проверки числа на четность
    if math.gcd(a,b)!=1: return 0  # Функция math.gcd() возвращает наибольший общий делитель указанных целочисленных аргументов *integers

    r = 1
    if a < 0:
        a = -a
        if b % 4 == 3:
            r = -r

    while True:
        t = 0
        while even(a):
            t += 1
            a //= 2
        
        if not even(t):
            if b%8 in (3,5):
                r = -r

        if a%4 == b%4 == 3:
            r =- r

        c = a
        a = b % c
        b = c

        if a==0: return r


def sol_shtassen(n):
    flag = True
    for i in range(10):
        a = randint(2, n - 1)
        r = (a**((n-1)/2)) % 2 
        if r != 1 and r != n - 1:
            flag = False
        jac = jacobi_symbol(a, n)
        if r == jac % n:
            flag = False 
        else:
            flag = True     
    if flag == True:
        return('Число n, вероятно, простое')
    else:
        return('Число n  составное')


def miller_robin(n):
    flag = True
    even = lambda x: x%2==0 
    r = n - 1 
    s = 0
    while even(r):
        s += 1
        r //= 2

    for i in range(10):
        a = randint(2, n - 2)

        y = (a ** r) % n
        if y != 1 and y != n - 1:
            j = 1
            if j <= s - 1 and y != n - 1:
                y = (y ** 2) % n
                if y == 1:
                    flag = False
                    break
                j += 1     
            if y != n - 1:
                flag = False
                break    
        flag = True
    if flag == True:
        return('Число n, вероятно, простое')
    else:
        return('Число n  составное')             

num = int(input())
#print('Resulr of Test Ferm:',test_ferm(num), end = '\n\n')
#print('Result of Solovey - Shtrassen:', sol_shtassen(num), end = '\n\n')
print('Result of Miller-Robin:', miller_robin(num),  end = '\n\n')
