n=input()
n=n.lower()
l=list(set(n))
c=0
for i in l:
    if i!=' ':
        c+=1
print(c)