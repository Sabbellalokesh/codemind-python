l=list(map(str,input().split()))
min=0
for i in range(len(l)):
    if len(l[i])>min:
        min=len(l[i])
print(min)