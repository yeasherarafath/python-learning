first=0
second=1
for i in range (8):
    third=first+second
    first=second
    second=third
    print(third)
