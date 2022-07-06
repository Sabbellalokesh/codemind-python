n=input()
m=input()
s=0
s1=0
for i in n:
    s=s+ord(i)
for i in m:
    s1=s1+ord(i)
if s==s1:
    print("True")
else:
    print("False")