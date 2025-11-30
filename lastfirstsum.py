

alist=[]
for i in range(1):
            a=input("Enter Intger Number: ")
            alist.append(a)
            c=len(alist[0])-1
            d=alist[0][0]
            e=alist[0][c]
            f=alist[0][0]+e
            g=(e)+(d)
            h=(int(g)/10)-0.1
            i=int(g)%10
#or cut for loop and make varibale c=1

print(int(h+i))