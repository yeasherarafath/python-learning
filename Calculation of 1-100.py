array = []
sum = 0
for i in range (0,5):
    element = int (input())
    array.append(element)
    sum = sum + element
min = array[0]
for i in range (0,5):
    if(array[i]<array[0]):
        min = array[i]
max = array[0]  
for i in range (0,5):
    if(array[i]>array[0]):
        max = array[i];
print(sum-max, sum-min)