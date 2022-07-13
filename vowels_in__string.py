n=input()
a=[]
s='aeiouAEIOU'
for i in n:
    if i in s:
        if i not in a:
            a.append(i)
print(*a)
    