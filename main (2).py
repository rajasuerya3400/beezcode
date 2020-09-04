print("Enter p and q ")
x=int(input())
y=int(input())
print("Before swapping")
print("m= "+str(x))
print("n= "+str(y))
x^=y 
y^=x 
x^=y 
print("After swapping")
print("m= "+str(x))
print("n= "+str(y))