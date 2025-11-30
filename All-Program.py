#Count total element of List:
list1=['physics','chemistry',1997,2000]
print(list1)
print(len(list1))
#Deleting List Element:
list1=['physics','chemistry',1997,2000]
print(list1)
del list1[2]
print('After deleting value at index 2:')
print(list1)
#prints complete list
list=[52,45.5,142,"Shanto",78,52,"Polytechnic"]
tinylist=[50,51,52,53,54,55,556,57,58,59]
print(list)
#prints concatenated lists
list=[52,45.5,142,"Shanto",78,52,"Polytechnic"]
tinylist=[50,51,52,53,54,55,556,57,58,59]
print(list+tinylist)
#prints element starting from 3rd element
list=[52,45.5,142,"Shanto",78,52,"Polytechnic"]
tinylist=[50,51,52,53,54,55,556,57,58,59]
print(list[2:])
#prints elements starting from 2nd till 3rd
list=[52,45.5,142,"Shanto",78,52,"Polytechnic"]
tinylist=[50,51,52,53,54,55,556,57,58,59]
print(list[1:3])
#prints first element of the list
list=[52,45.5,142,"Shanto",78,52,"Polytechnic"]
tinylist=[50,51,52,53,54,55,556,57,58,59]
print(list[0])
#prints list two times
list=[52,45.5,142,"Shanto",78,52,"Polytechnic"]
tinylist=[50,51,52,53,54,55,556,57,58,59]
print(tinylist*2)
#Updating Lists/Replacement of data:
list=['physics','chemistry',1997,2000];
print('Value available at index 2:') 
print(list[2])
list[2]=2001;
print('New value available at index 2:')
print(list[2]) 