x=int(input())
y=list(map(int,input().split()))
y.sort()
print(y[-1]*y[-2])