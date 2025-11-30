#Area of a Tringle
a=float(input("Enter a Number: "))
b=float(input("Enter a Number: "))
c=float(input("Enter a Number: "))
if a+b>c and b+c> a and a+c>b:
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("area)
else:
    print("This is not a Tringle")