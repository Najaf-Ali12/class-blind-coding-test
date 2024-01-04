
#make a programme that tell the factorial of user inputted number
#with both for and while loops
#1:using for loop
n=int(input("enter a number whose factorial you want"))
s=1
if n>0:
    for i in range(1,n+1):
      s=s*i
else:
    print("for getting factorial number must be postive and not equals to zero")
print("the factorial of",n,"is",s)


#using while loop
a=int(input("number=?,whose factorial you want"))
factorial=1
if a<0:
    print("input a positive number")
else:
    while a>0:
        factorial*=a
        a-=1
print("the factorial of your given number is",factorial)

