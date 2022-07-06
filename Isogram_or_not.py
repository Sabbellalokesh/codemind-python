n=input()
s=0
for i in range(len(n)):
    c=0
    for j in range(len(n)):
        if n[i]==n[j]:
            c+=1
    if c>1:
        s+=1
if s>0:
    print("False")
else:
    print("True")