marks=[14,41,55,5,6565,55,525,55441,7712,8582252,8485,8752,7984,978,456,55]
loc=-1
a=int(input("Enter: "))
for i in range(1,len(marks)):
    if a==marks[i]:
        loc=i
        print(loc)
if loc==-1:
    print("Not Found")