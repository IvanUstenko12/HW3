from math import log2, floor
def func(s, p):
    #print(s, p)
    global otv, f, n
    if len(s) == 1:
        if s[0] == n:
            otv.append(p)
    else:
        s1 = []
        s2 = []
        for i in range (1, f - len(p) + 1):
            for k in range(2**(i-1)):
                s1.append(s[2**i - 1 + k])
            for k in range(2**(i-1), 2**i):
                s2.append(s[2**i - 1 + k])
        p1 = p.copy()
        p2 = p.copy()
        if s1[0] != '':
            p1.append(s1[0])
            s1[0] += s[0]
            func(s1, p1)
        if s2[0] != '':
            p2.append(s2[0])
            s2[0] += s[0]
            func(s2, p2)

otv = []
s = input().split(',')
for i in range(len(s)):
    if s[i].isdigit():
        s[i] = int(s[i])     
i = 0  
while len(s) > 2**(i + 1):
    for k in range(2**i - 1, 2**(i + 1) - 1):
        if s[k] == '':
            s.insert(2*k + 1, '')
            s.insert(2*k + 2, '')
    i += 1
for _ in range(len(s) - 2**floor(log2(len(s) + 1)) + 1):
    del s[-1]
f = floor(log2(len(s) + 1))
n = int(input())
func(s, [s[0]])
for i in range(len(otv)):
    sa = otv[i].copy()
    for k in range(len(sa)):
        sa[k] = str(sa[k])
    print('->'.join(sa))