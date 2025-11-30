a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
if a>b and a>c:
    print(a, "is larger than" , b , c)
elif b>a and b>c:
    print(b, "is larger than" , a , c)
else:
    print(c, "is larger than" , a , b)
    
