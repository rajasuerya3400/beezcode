m=int(input())
n=int(input())
q=0
for i in range(m,n+1):
    q+=list(str(i)).count("1")
print(q)    