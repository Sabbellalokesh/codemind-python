l=list(map(str,input().split()))
c=0
for i in range(len(l)):
    l[i]=l[i].lower()
    x=l[i][::-1]
    if l[i]==x:
        c+=1
print(c)