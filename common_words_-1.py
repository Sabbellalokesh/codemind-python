l=list(map(str,input().split()))
ll=list(map(str,input().split()))
s=0
for i in range(len(l)):
    l[i]=l[i].lower()
for i in range(len(ll)):
    ll[i]=ll[i].lower()
for i in l:
    c=0
    for j in ll:
        if i==j:
            c+=1
    if c>0:
        s+=1
print(s)   