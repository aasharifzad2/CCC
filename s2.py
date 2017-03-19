N = input()
s = raw_input()
s = s.split()
g1 = []
for i in range(N):
    g1.append(int(s[i]))
high = []
low = []

rr = 0
for i in range(N/2):
    if g1[rr] > g1[rr+1]:
        high.append(g1[rr])
        low.append(g1[rr+1])
    else:
        high.append(g1[rr+1])
        low.append(g1[rr])
    rr +=2

high = sorted(high)
low = sorted(low)
low.reverse()

alll = []
for i in range(N/2):
    alll.append(low[i])
    alll.append(high[i])
for i in alll:
    print i,
