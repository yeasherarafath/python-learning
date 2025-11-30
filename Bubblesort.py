def bubblesort(list):
    for passnum in range (len(list)-1,0,-1):
        for i in range (passnum):
            if list[i]>list[i+1]:
                temp=list[i]
                list[i]=list[i+1]
                list[i+1]=temp
list=[21,54,48,52,45,62,12,64,25,54,8,4,1,55,25,80,13,61,24,25,52,42,4,0]
print(list)
bubblesort(list)
print(list)