value=int(input("Enter a Number for Searching: "))
alist=[1,25,241,36,28,25,24]
if value in alist:
    print("value in list", "address: " "alist[",alist.index(value),"]", alist.count(value))
else:
    print("value exit in list")

