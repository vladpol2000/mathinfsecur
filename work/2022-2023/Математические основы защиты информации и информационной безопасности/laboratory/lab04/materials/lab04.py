def evklid(a, b, d):
    for i in range(1, b + 1):
        if a % i == 0 and b % i == 0:
            d = i
        else:
            continue
    return d


def binary_evklid(a, b):
    g = 1
    while ( a % 2 == 0 and b % 2 == 0):
        a, b, g = a // 2, b // 2, g * 2
    while a != 0:
        while a % 2 == 0:
            a = a // 2
        while b % 2 == 0:
            b = b // 2    
        if a >= b:
            a = a - b
        else:
            b = b - a
    return b * g


def extend_evklid(a, b):
    r0 = a
    r1 = b
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1
    i = 1

    while r1!=0:
        q = r0//r1
        r0 = r0%r1
        r0, r1 = r1, r0

        x0 -= q*x1
        x0, x1 = x1, x0 

        y0 -= q*y1
        y0, y1 = y1, y0
    return r0, x0, y0


def extend_binary_evklid(a, b):
    g = 1
    while ( a % 2 == 0 and b % 2 == 0):
        a, b, g = a // 2, b // 2, g * 2

    u, v = a, b
    A, B, C, D = 1, 0, 0, 1

    while u != 0:
        while u % 2 == 0:
            u //= 2
            if A % 2 == 0 and B % 2 == 0:
                A, B = A//2, B//2
            else:
                A = (A + b) // 2 
                B = (B - a) // 2
        while v % 2 == 0:
            v //= 2
            if C % 2 == 0 and D % 2 == 0:
                C, D = C//2, D//2
            else:
                C = (C + b) // 2 
                D = (D - a) // 2
        if u >= v:
            u -= v
            A -= C
            B -= D
        else:
            v -= u
            C -= A
            D -= B
    d = g*v
    x = C
    y = D
    return d,x,y



a, b, d = int(input()), int(input()), 0

print('Result of Evklid algorithm is', evklid(a, b, d), end = '\n\n')            
print('Result of Binary Evklid algorithm is', binary_evklid(a, b), end = '\n\n')
print('Result of Extend Evklid algorithm is', extend_evklid(a, b), end = '\n\n')
print('Result of Extend Binary Evklid algorithm is', extend_binary_evklid(a, b), end = '\n\n')