a=int(input("Input a number: "))
b=int(input("Input a number: "))
c=int(input("Input a number: "))
if a>b and a>c:
    print(a, "is biggest")
elif b>a and b>c:
    print(b, "is biggest")
else:
    print (c, 'is biggest')