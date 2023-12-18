#write a python programmes that takes two numbers as input and calculate the sum of their
#squares only if both numbers are odd.If any one the numbers is even,print a message
#indicating that the calculation is not performed.
n1=int(input("enter your first number"))
n2=int(input("enter your second number"))
if n1%2==1 and n2%2==1:
    print("the sum of square of",n1,"and",n2,"is",n1**2+n2**2)
else:
    print("calculation is not performed")
#we can also write this programme in which we will tell that which number is even
    #either n1 or n2 when we have inputted two values
if n1%2==0:
    print("n1 is even")
if n2%2==0:
    print("n2 is even")
        
else:
    print(n1**2+n2**2)
#we can also write it as under
if n1%2!=0:
    if n2%2!=0:
        print(n1**2+n2**2)
else:
    print("the calculation is not performed")
        
    

