l=list(map(str,input().split()))
a=[]
ll=len(l)
a.append(min(l[0]))
a.append(max(l[ll-1]))
print(*a)