#QNO:1
#to make a programme that will delect our 
#duplicate elements of list without using
list1=[1,3,2,5,6,4,7,8,9,6,9,6,3]
empty=[]
for i in list1:
    if i not in empty:
      empty.append(i)
      empty.sort()
print(empty)
#OR
#by converting list in set because in set no repetition happens
list1=set([2,4,5,6,7,8,9,1,2,5,6,8,4,3])
print(list1)
