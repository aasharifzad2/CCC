N = input()
swi = raw_input()
sem = raw_input()
swi = swi.split()
sem = sem.split()
g1 = []
g2 = []


for i in range(len(swi)):
    g1.append(int(swi[i]))
    g2.append(int(sem[i]))

def addd(x):
    g = []
    for i in range(1,N+1):
        g.append(sum(x[0:i]))
    return g

sum1 = addd(g1)
sum2 = addd(g2)

haha = []
for i in range(N):

    if sum1[i] == sum2[i]:
        haha.append(i+1)
if len(haha) > 0:
    print haha[-1]
else:
    print 0
