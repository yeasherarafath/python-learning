input=int(input("Enter Your Range: "))
first, second=0,1
for i in range(input):
    third=first+second
    print(third)
    first=second
    second=third
