l=list(map(str,input().split()))
ll=len(l)
a=[]
for i in range(ll):
    a.append(min(l[i]))
    a.append(max(l[i]))
print(*a)