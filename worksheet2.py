#question 1
L = [11, 12, 13, 14]
L.append(50)
L.append(60)
print(L)

L.remove(11)
L.remove(13)
print(L)

L.sort()
print(L)

L.sort(reverse=True)
print(L)

# Search 13
flag = 0
for i in L:
    if i == 13:
        flag = 1
if flag == 1:
    print("NUMBER FOUND")
else:
    print("NUMBER NOT FOUND")

# Count
count = 0
for i in L:
    count += 1
print("COUNT : ", count)

# Even & Odd Sum
sumo = 0
sume = 0
for i in L:
    if i % 2 == 0:
        sume += i
    else:
        sumo += i
print("EVEN SUM : ", sume)
print("ODD SUM : ", sumo)

# Prime Sum
sump = 0
for i in L:
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0 and i > 1:
        sump += i
print("SUM PRIME : ", sump)

# Clear List
L.clear()
del(L)

#question 2
L = [2, 4, 6, 8]

s = 0
for x in L:
    s = s + x

print("SUM:", s)

#question 3
L = [2, 4, 6, 8]

m = 1
for x in L:
    m = m * x

print("MUL:", m)

#question 4
a = []
for i in range(3):
    b = []
    for j in range(4):
        c = []
        for k in range(6):
            c.append("*")
        b.append(c)
    a.append(b)

print(a)

#question 5
D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}

# (i)
D[8] = 8.8
print(D)

# (ii)
del D[2]
print(D)

# (iii)
if 6 in D:
    print("YES")
else:
    print("NO")

# (iv)
c = 0
for k in D:
    c = c + 1
print("COUNT:", c)

# (v)
s = 0
for k in D:
    s = s + D[k]
print("SUM:", s)

# (vi)
D[3] = 7.1
print(D)

# (vii)
D.clear()
print(D)

#question 6
S1 = {10,20,30,40,50,60}
S2 = {40,50,60,70,80,90}

# (i)
S1.add(55)
S1.add(66)
print(S1)

# (ii)
S1.remove(10)
S1.remove(30)
print(S1)

# (iii)
if 40 in S1:
    print("YES")
else:
    print("NO")

# (iv)
print(S1 | S2)

# (v)
print(S1 & S2)

# (vi)
print(S1 - S2)

#question 7
import random
import string

for i in range(100):
    ln = random.randint(6,8)
    st = ""
    for j in range(ln):
        st = st + random.choice(string.ascii_letters)
    print(st)
for x in range(600,801):
    f = 0
    for j in range(2,x):
        if x % j == 0:
            f = 1
            break
    if f == 0:
        print(x)
for x in range(100,1001):
    if x % 7 == 0 and x % 9 == 0:
        print(x)

#question 8
exam_st_date = (11,12,2025)
print("The examination will start from:", exam_st_date[0], "/", exam_st_date[1], "/", exam_st_date[2])

#question 9
L = [10,23,45,50,77,90]
for x in L:
    if x % 5 == 0:
        print(x)

#question 10
n = 7
b = (n % 2 == 0)
if b == True:
    print("EVEN")
else:
    print("ODD")

#question 11
txt = "Emma is good. Emma plays chess. Emma is nice."
c = 0
for i in range(len(txt)-3):
    if txt[i:i+4] == "Emma":
        c = c + 1
print("COUNT:", c)

#question 12
L1 = [1,2,3,4,5]
L2 = [6,7,8,9,10]
L3 = []

for x in L1:
    if x % 2 != 0:
        L3.append(x)

for x in L2:
    if x % 2 == 0:
        L3.append(x)

print(L3)

#question 13
pos = [(2,3),(4,5),(6,7),(7,8)]
for p in pos:
    if p[0] % 2 == 0:
        print(p)

#question 14
data = {1:2.3, 2:4.5, 3:1.8, 4:3.6}
for k in data:
    if data[k] > 3.0:
        print(k)

#question 15
rec = {"MOVE","TURN_LEFT","TURN_RIGHT","STOP"}
exe = {"MOVE","TURN_LEFT","STOP"}

for x in rec:
    if x not in exe:
        print(x)