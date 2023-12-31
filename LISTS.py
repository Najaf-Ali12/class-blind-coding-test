#CREATE A PYTHON LLST,ADD MULTIPLE VALUES AND REMOVE THE DUPLICATED VALUES FROM
#THE LIST,AND PRINT THE FINAL LIST.DONOT USE THE PYTHON BUILTIN FUNCTIONS.
a=[1,2,3,4,5,6,3,6]
emptylist=[]
x=0
for i in a:
    print(i+x)
    x+=i
    if i not in emptylist:
        emptylist.append(i)
print(emptylist)






    
    
    
















