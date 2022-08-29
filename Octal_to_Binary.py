t=int(input())
for i in range(t):
    n=int(input())
    s=0
    i=0
    l=[]
    while n!=0:
        r=n%10
        s=s+(r*(8**i))
        i+=1
        n=n//10
    j=0
    while s!=0:
        r=s%10
        a=r%2
        l.append(a)
        s=s//2
    l.reverse()
    for i in l:
        print(i,end='')
    print()