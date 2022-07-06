l=list(map(str,input().split()))
a=[]
for i in range(len(l)):
    a.append(ord(max(l[i]))-ord(min(l[i])))
print(*a)