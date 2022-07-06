n=input()
n=n.lower()
a=[]
for i in range(len(n)):
    c=0
    for j in range(len(n)):
        if n[i]==n[j] and n[i]!=' ':
            c+=1
    if c==1:
        a.append(n[i])
a.sort()
for i in range(len(a)):
    print(a[i],end='')