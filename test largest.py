marks=[14,41,55,5,6565,55,525,55441,7712,8582252,8485,8752,7984,978,456]
largest=marks[0]
for i in range(1, len(marks)):
    if largest<marks[i]:
        largest=marks[i]
print(largest)