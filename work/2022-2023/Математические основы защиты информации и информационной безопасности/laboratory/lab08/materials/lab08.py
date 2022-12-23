import math

def first_alg():
    u = '234'
    v = '156'
    b = 10
    n = 3

    j = n
    k = 0

    w = list()
    for i in range(1, n + 1):
        w.append((int(u[n-i]) + int(v[n-i]) + k) % b)
        k = (int(u[n-i]) + int(v[n-i]) + k) // b
        j = j - 1
    w.reverse()
    print('Result of first algorthm:', w)


def second_alg():
    u = '456'
    v = '123'
    b = 10
    n = 3

    j = n
    k = 0

    w = list()
    for i in range(1, n + 1):
        w.append((int(u[n-i]) - int(v[n-i]) + k) % b)
        k = (int(u[n-i]) - int(v[n-i]) + k) // b
        j = j - 1
    w.reverse()
    print('Result of second algorthm:', w)
    


u = '1234'
v = '89'
n = 4
m = 2

w = list()
for i in range(m + n):
    w.append(0)
j = m

def s_6():    
    global w
    global j
    j = j - 1
    if j > 0:
        s_2()
    if j == 0:
        print(w) 

def s_2():
    global v 
    global w
    global j
    if j == m:
        j = j - 1
    if int(v[j]) == 0:
        s_6()   

def s_4():
    b = 10
    global k
    global t
    global i
    if i == n:
        i -= 1
    t = int(u[i])*int(v[j]) + w[i+j] + k    
    w[i+j] = t % b
    k = t / b

def s_5():
    global i
    global w
    global j
    global k
    i = i - 1
    if i > 0:
        s_4()
    else:
        w[j] = k

s_2()
i = n
k = 0
t = 1
s_4()
s_5()
s_6()
print('Result of third algorthm:', w)

def th_alg():
    u4 = "12345"
    n = 5
    v4 = "6789"
    m = 4
    b = 10
    w1 = list()
    for i in range(m+n+2):
        w1.append(0)
    t1 = 0
    for s1 in range(0, m+n):
        for i1 in range(0, s1+1):
            if n-i1>n or m-s1+i1>m or n-i1<0 or m-s1+i1<0 or m-s1+i1-1<0:
                continue
            t1 = t1 + (int(u4[n-i1-1]) * int(v4[m-s1+i1-1]))
        w1[m+n-s1-1] = t1 % b
        t1 = math.floor(t1/b)
    print('Result of th algorthm:', w1)




u = "12346789"
n = 7
v = "56789"
t = 4
b = 10
q = list()
for j in range(n-t):
    q.append(0)
r = list()
for j in range(t):
    r.append(0)

while int(u) >= int(v)*(b**(n-t)):
    q[n-t] = q[n-t] + 1
    u = int(u) - int(v)*(b**(n-t))
u = str(u)
for i in range(n, t+1, -1):
    v = str(v)
    u = str(u)
    if int(u[i]) > int(v[t]):
        q[i-t-1] = b - 1
    else:
        q[i-t-1] = math.floor((int(u[i])*b + int(u[i-1]))/int(v[t]))

    while (int(q[i-t-1])*(int(v[t])*b + int(v[t-1])) > int(u[i])*(b**2) + int(u[i-1])*b + int(u[i-2])):
        q[i-t-1] = q[i-t-1] - 1
    u = (int(u) - q[i-t-1]*b**(i-t-1)*int(v))
    if u < 0:
        u = int(u) + int(v) *(b**(i-t-1))
        q[i-t-1] = q[i-t-1] - 1
r = u
print('Result of fifth algorthm:', q, r)



first_alg()
second_alg() 
th_alg()




