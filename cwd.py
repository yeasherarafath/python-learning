first, second=0,1
for i in range(100000):
    third=first+second
    print(third)
    first=second
    second=third

