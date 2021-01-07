b,a=map(int,input().split())
temp=0
x=min(a,b)
y=max(a,b)
while x!=0 and y!=0:
    temp=x
    x=y%x
    y=temp
print(temp)