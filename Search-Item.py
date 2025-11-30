s=[22,44,55,66,22,33,44,55,88,78,67,66,45]
find=int(input("Enter a variable:"))
if find in s:
            print(find, "is in s")
            for dpi in range(0,len(s)):
                if find==s[dpi]:
                    print(find, "is in position",dpi+1)
else:
            print(find, "is not in s")h