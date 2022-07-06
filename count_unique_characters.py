n=input()
cc=0
n=n.lower()

for i in range(len(n)):
    c=0
    for j in range(len(n)):
        if n[i]==n[j] and n[i]!=' ':
            c+=1
    if c==1:
        cc+=1
print(cc)