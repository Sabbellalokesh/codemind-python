l=list(map(str,input().split()))
c=0
for i in l:
    if i[0] in 'aeiouAEIOU':
        if i[len(i)-1] not in 'aeiouAEIOU':
            c+=1
print(c)