x=list(map(int,input().split(" ")))
x.sort()
for i in range(0,len(x)):
    if i+1 != x[i]:
        print(i+1)
        break;