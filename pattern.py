r=int(input("Enter the no. of rows:"))
c=int(input("Enter the no. of columns:"))
l=[]
for i in range(r):
    tl=[]
    for j in range(c):
        e=int(input(f"Enter the element{j+1}:"))
        tl.append(e)
    l.append(tl)
for k in range(r):
    s=0
    for a in range(c):
        d=[k][a]
        s+=d
    print("sum of ",a+1,"is",s)
for b in range(c):
    s=0
    for m in range(r):
        s+=l[b][m]
        print("sum of ",m+1,"is",s)
for f in range(r):
    s=0
    s1=0
    for g in range(c):
        s1+=l[g][b]
        s+=s1
    print("Sum of all elements is:",s)