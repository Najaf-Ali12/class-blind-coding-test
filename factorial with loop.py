a=int(input("enter a number"))
factorial=1
if a<=0:
    print("please enter a positive number")
else:
    for i in range(1,a+1):
        factorial=i*factorial
    print("your number is" ,a,"\n factorial of your number is",factorial)
    
