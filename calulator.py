def add(a,b):
    return a+b
def substrack(a,b):
    return a-b
def multipay(a,b):
    return a*b
def divide(a,b):
    return a/b

print("Select and Opreation")
print("1. Add")
print("2. Substrack")
print("3. Multipay")
print("4. Divide ")
x=input("Enter Your Choice: ")
num1=int(input("Enter Your First Number: "))
num2=int(input("Enter Your Second Number: "))
if x=='1':
    print(num1, "+", num2 ,"=",add(num1,num2))
elif x=='2':
    print(num1, "-", num2 ,"=",substrack(num1,num2))
elif x=='3':
    print(num1, "*", num2 ,"=",multipay(num1,num2))
elif x=='4':
    print(num1, "/", num2 ,"=",divide(num1,num2))
else:
    print("Bad Calculator Choice")